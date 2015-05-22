import datetime

from backend import db
from backend.models import User, Session, Product
from backend.models import Event, Order
from backend.models import UserCartProduct
from backend.utils import ModelTestCase


class TestUser(ModelTestCase):
    def test_create_user(self):
        """ Test that a user can be created.
        """
        user = self.create_user()
        db.session.add(user)
        db.session.commit()

        fetched_user = User.query.one()
        self.assertEqual(fetched_user, user)

    def test_user_deletion_deletes_sessions(self):
        """ Test that deleting a user also deletes that 
        users sessions."""
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        token = 'abcd'
        another_token = 'bcde'

        user = self.create_user()
        session = Session(expires_on=tomorrow, user=user, token=token)
        another_session = Session(expires_on=tomorrow, user=user, token=another_token)

        db.session.add(user)
        db.session.commit()

        fetched_user = User.query.one()
        self.assertEqual(set(fetched_user.sessions), set([session, another_session]))

        db.session.delete(fetched_user)
        # TODO: why is this commit not needed?
        #db.session.commit()
        self.assertEqual(Session.query.all(), list())

    def test_user_cart_product_creation(self):
        """ Test that a user can add a product to her cart.
        """
        user = self.create_user()
        product = self.create_product(name='abc', price_rands=99)
        user.cart_products.append(product)
        db.session.add(user)
        db.session.commit()

        product = Product.query.one()
        self.assertEqual(product, user.cart_products[0])

    def test_user_deletion_deletes_user_cart_products(self):
        """ Test that deleting a user deletes her cart_products.
        """
        user = self.create_user()
        product = self.create_product(name='abc', price_rands=99)
        user.cart_products.append(product)
        db.session.add(user)
        db.session.commit()

        user = User.query.one()

        self.assertEqual(product, user.cart_products[0])

        db.session.delete(user)
        db.session.commit()

        self.assertEqual(User.query.all(), list())
        self.assertEqual(UserCartProduct.query.all(), list())
        fetched_product = Product.query.first()

        self.assertEqual(fetched_product, product)

    def test_user_deletion_keeps_events(self):
        """ Test that deleting a user keeps that 
        users current_cart_event."""

        user = self.create_user()
        event = self.create_event(name='test_product')

        event.users.append(user)
        db.session.add(event)
        db.session.commit()

        self.assertEqual(User.query.one().current_cart_event, event)

        db.session.delete(user)
        db.session.commit()

        self.assertEqual(Event.query.one(), event)

    def test_user_order_creation(self):
        """ Test that a user can have orders.
        """
        user = self.create_user()
        event = self.create_event(name='test_product')
        order = self.create_order()
        order.event = event

        user.orders.append(order)
        db.session.add(user)
        db.session.commit()

        order = Order.query.one()
        self.assertEqual(User.query.one().orders, [order])
        