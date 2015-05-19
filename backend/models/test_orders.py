import datetime

from backend import db
from backend.models import Event, User, Order
from backend.models import UserCartProduct
from backend.utils import ModelTestCase


class TestOrder(ModelTestCase):
    def test_create_order(self):
        """ Test that an Order can be created.
        """
        order = self.create_order()
        event = self.create_event(name='test')
        user = self.create_user()
        order.user = user
        order.event = event
        db.session.add(order)
        db.session.commit()

        fetched_order = Order.query.one()
        self.assertEqual(fetched_order, order)

    def test_order_deletion_keeps_users_and_events(self):
        """ Test that deleting an Order which has 
        users does not delete those users.
        """
        user = self.create_user()
        event = self.create_event(name='test')
        order = self.create_order()
        order.event = event

        user.orders.append(order)
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

