import datetime

from backend import db
from backend.models import Event, User, Order
from backend.models import Cart
from backend.testing import ModelTestCase


class TestOrder(ModelTestCase):
    def test_order_total_rands(self):
        """ Test that Order.total_rands is equal to the sum
        of all OrderProduct.sub_total_rands for an Order.
        """
        event = self.create_event(name='test')
        price = 10
        product_1 = self.create_product(create_valid_product=True, price_rands=price)
        product_2 = self.create_product(create_valid_product=True, price_rands=price)
        order = self.create_order(
            event=event,
        )
        order_product_1 = self.create_order_product(
            unit_price_rands=product_1.price_rands,
            quantity=1,
            order=order,
            product=product_1,
        )
        order_product_2 = self.create_order_product(
            unit_price_rands=product_2.price_rands,
            quantity=2,
            order=order,
            product=product_2,
        )
        user = self.create_user(normal_user=True, orders=[order], with_cart=True)
        db.session.add(user)
        db.session.commit()
        fetched_order = Order.query.one()
        self.assertEqual(fetched_order.total_rands, price * 3)

    def test_from_cart(self):
        """ Test that Order.from_cart creates an order
        from a Cart.
        """
        user = self.create_user(normal_user=True, with_cart=True)
        product = self.create_product(create_valid_product=True, price_rands=11)
        event = self.create_event(name='qwe')
        user.cart.event = event
        user.cart.products.append(product)
        db.session.add(user)
        db.session.commit()
        order = Order()
        order.from_cart(user.cart)
        db.session.add(order)
        db.session.commit()
        self.assertEqual(order.total_rands, 11)
        self.assertEqual(order.products, [product])
