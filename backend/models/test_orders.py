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
        product_1 = factories.ProductFactory(price_rands=price)
        product_2 = factories.ProductFactory(price_rands=price)
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
            quantity=1,
            product=product_1,
        )
        order_product_2 = factories.OrderProductFactory(
            unit_price_rands=product_2.price_rands,
            order=order,
            quantity=1,
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
        product_1 = factories.ProductFactory(price_rands=1)
        product_2 = factories.ProductFactory(price_rands=2)
        festival = factories.FestivalFactory()
        quantity_1 = 7
        quantity_2 = 4
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

        self.assertEqual(order.total_rands, 15)
        order_product_1 = (db.session.query(
            OrderProduct)
            .filter(OrderProduct.order == order)
            .filter(OrderProduct.product == product_1)
            .one())
        self.assertEqual(order_product_1.quantity, quantity_1)

        order_product_2 = (db.session.query(
            OrderProduct)
            .filter(OrderProduct.order == order)
            .filter(OrderProduct.product == product_2)
            .one())
        self.assertEqual(order_product_2.quantity, quantity_2)
