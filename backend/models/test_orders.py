import datetime

from backend import db
from backend.models import Event, User, Order
from backend.models import Cart
from backend.testing import ModelTestCase


class TestOrder(ModelTestCase):
    def test_create_order(self):
        """ Test that an Order can be created.
        """
        
        event = self.create_event(name='test')
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        order = self.create_order(user=user, event=event)
        db.session.add(order)
        db.session.commit()

        fetched_order = Order.query.one()
        self.assertEqual(fetched_order, order)

    def test_order_deletion_keeps_users_and_events(self):
        """ Test that deleting an Order which has 
        users does not delete those users.
        """
        event = self.create_event(name='test')
        order = self.create_order(event=event)
        user = self.create_user(create_normal_user=True, orders=[order], create_valid_cart=True)
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.one(), user)
        self.assertEqual(User.query.one().orders, [order])

        db.session.delete(order)
        db.session.commit()

        self.assertIsNone(Order.query.first())

        self.assertEqual(User.query.one(), user)
        self.assertEqual(User.query.one().orders, list())

        self.assertEqual(Event.query.one(), event)

    def test_order_total_rands(self):
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
            quantity=1,
            order=order,
            product=product_2,
            )
        user = self.create_user(create_normal_user=True, orders=[order], create_valid_cart=True)
        db.session.add(user)
        db.session.add(order_product_1)
        db.session.add(order_product_2)
        db.session.commit()

        fetched_order = Order.query.one()
        self.assertEqual(fetched_order.total_rands, price * 2)

    def test_from_cart(self):
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
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
