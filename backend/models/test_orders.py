from sqlalchemy import func

from backend import db
from backend.testing import ModelTestCase
from backend.testing import factories

from . import Order, OrderProduct


class TestOrder(ModelTestCase):
    def test_order_total_rands(self):
        """ Test that Order.total_rands is equal to the sum
        of all OrderProduct.sub_total_rands for an Order.
        """
        festival = factories.FestivalFactory()
        price = 10
        product_1 = factories.ProductFactory(
            product_prices=[
                factories.ProductPriceFactory(amount_rands=price),
            ],
        )
        product_2 = factories.ProductFactory(
            product_prices=[
                factories.ProductPriceFactory(amount_rands=price),
            ],
        )
        db.session.add(product_1)
        db.session.add(product_2)
        db.session.commit()
        user = factories.UserFactory()
        order = factories.OrderFactory(
            user=user,
            festival=festival,
        )
        order_product_1 = factories.OrderProductFactory(
            unit_price_rands=product_1.price_rands,
            order=order,
            product=product_1,
        )
        order_product_2 = factories.OrderProductFactory(
            unit_price_rands=product_2.price_rands,
            order=order,
            product=product_2,
        )
        db.session.add(user)
        db.session.commit()
        fetched_order = Order.query.one()
        self.assertEqual(fetched_order.total_rands, price * 2)

    def test_from_cart(self):
        """ Test that Order.from_cart creates an order
        from a Cart.
        """
        user = factories.UserFactory()
        product_1 = factories.ProductFactory(
            product_prices=[
                factories.ProductPriceFactory(amount_rands=1),
            ],
        )
        product_2 = factories.ProductFactory(
            product_prices=[
                factories.ProductPriceFactory(amount_rands=2),
            ],
        )
        festival = factories.FestivalFactory()
        quantity_1 = 1
        quantity_2 = 2
        user.cart.festival = festival
        cart_product_1 = factories.CartProductFactory(
            cart=user.cart,
            product=product_1,
            quantity=quantity_1,
        )
        cart_product_2 = factories.CartProductFactory(
            cart=user.cart,
            product=product_2,
            quantity=quantity_2,
        )
        db.session.add(cart_product_1)
        db.session.add(cart_product_2)
        db.session.add(user)
        db.session.commit()

        order = Order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()

        self.assertEqual(order.total_rands, 5)
        order_product_1, order_product_1_quantity = (db.session.query(
            OrderProduct, func.count(OrderProduct.product_id))
            .filter(OrderProduct.order == order)
            .filter(OrderProduct.product == product_1)
            .group_by(OrderProduct.product_id)
            .one())
        self.assertEqual(order_product_1_quantity, quantity_1)

        order_product_2, order_product_2_quantity = (db.session.query(
            OrderProduct, func.count(OrderProduct.product_id))
            .filter(OrderProduct.order == order)
            .filter(OrderProduct.product == product_2)
            .group_by(OrderProduct.product_id)
            .one())
        self.assertEqual(order_product_2_quantity, quantity_2)
