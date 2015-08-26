import datetime

from backend import db
from backend.models import User, Session, Product
from backend.models import Event, Order, Cart
from backend.testing import ModelTestCase


class TestUser(ModelTestCase):
    def test_create_user(self):
        """ Test that a user can be created.
        """
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        db.session.add(user)
        db.session.commit()

        fetched_user = User.query.one()
        self.assertEqual(fetched_user, user)

    def test_user_is_not_guest(self):
        user = self.create_user(email_address='asd@asd.com', create_valid_cart=True)
        user.first_name = 'Asd'
        user.set_password('123')
        db.session.add(user)
        db.session.commit()
        self.assertFalse(user.is_guest)

    def test_user_is_guest_with_email(self):
        user = self.create_user(email_address='asd@asd.com', create_valid_cart=True)
        user.guest_token = 'jasduqwejj'
        user.email_address = 'asd@asd.com'
        user.first_name = 'Asd'
        user.set_password('asd')
        db.session.add(user)
        db.session.commit()
        self.assertFalse(user.is_guest)

    def test_user_is_guest(self):
        user = self.create_user(create_valid_cart=True)
        user.guest_token = 'jasduqwejj'
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.is_guest)

    def test_user_deletion_deletes_sessions(self):
        """ Test that deleting a user also deletes that 
        users sessions."""
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        token = 'abcd'
        another_token = 'bcde'

        user = self.create_user(create_normal_user=True, create_valid_cart=True)
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
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        product = self.create_product(create_valid_product=True)
        user.cart = Cart(products=[product])
        db.session.add(user)
        db.session.commit()

        product = Product.query.one()
        self.assertEqual(product, user.cart.products[0])

    def test_user_deletion_deletes_user_cart_products(self):
        """ Test that deleting a user deletes her cart_products.
        """
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        product = self.create_product(create_valid_product=True)
        user.cart = Cart(products=[product])
        db.session.add(user)
        db.session.commit()

        user = User.query.one()

        self.assertEqual(product, user.cart.products[0])

        db.session.delete(user)
        db.session.commit()

        self.assertEqual(User.query.all(), list())
        self.assertEqual(Cart.query.all(), list())
        fetched_product = Product.query.first()

        self.assertEqual(fetched_product, product)

    def test_user_order_creation(self):
        """ Test that a user can have orders.
        """
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        event = self.create_event(name='test_product')
        order = self.create_order()
        order.event = event

        user.orders.append(order)
        db.session.add(user)
        db.session.commit()

        order = Order.query.one()
        self.assertEqual(User.query.one().orders, [order])

    def test_user_check_constraint_as_guest(self):
        """ Test the CheckConstraint on User,
        either:
            1) guest_token can be not null, then email_address, password and first_name can be null
            2) email_address, password, first_name can be not null, then guest_token can be null
        """

        user = User()
        user.cart = Cart()
        user.guest_token = 'asd'
        db.session.add(user)
        db.session.commit()

    def test_user_check_constraint_non_guest(self):
        """ Test the CheckConstraint on User,
        either:
            1) guest_token can be not null, then email_address, password and first_name can be null
            2) email_address, password, first_name can be not null, then guest_token can be null
        """

        user = User()
        user.cart = Cart()
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        self.assertEqual(User.query.first(), None)

        user = User()
        user.cart = Cart()
        user.email_address = 'asd'
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        self.assertEqual(User.query.first(), None)

        user = User()
        user.cart = Cart()
        user.first_name = 'asd'
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        self.assertEqual(User.query.first(), None)

        user = User()
        user.cart = Cart()
        user.set_password('asd')
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        self.assertEqual(User.query.first(), None)

        user = User()
        user.cart = Cart()
        user.email_address = 'asd'
        user.set_password('asd')
        user.first_name = "test"
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.first(), user)
