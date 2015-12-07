import datetime

from backend import db
from backend.testing import BackendTestCase
from backend.models import User, Session, Cart
from backend.models import Product


class TestBackendTestCaseCreateProduct(BackendTestCase):
    def test_create_product_creates_valid_product(self):
        """ Test that create_product creates a valid Product,
        with name, cost_rands and price_rands pre-populated
        for convenience.
        """
        product = self.create_product(create_valid_product=True)
        db.session.add(product)
        db.session.commit()
        fetched_product = Product.query.first()
        self.assertIsNotNone(fetched_product)


class TestBackendTestCaseCreateSession(BackendTestCase):
    def test_create_session_creates_session(self):
        """ Test create_session creates a session.
        """
        now = datetime.datetime.now()
        expires_on = now + datetime.timedelta(seconds=30)
        user = self.create_user(normal_user=True, with_cart=True)
        session = self.create_session(
            expires_on=expires_on,
            user=user,
        )
        session.generate_token()
        db.session.add(session)
        db.session.commit()
        fetched_session = Session.query.first()
        self.assertIsNotNone(fetched_session)
        self.assertEqual(fetched_session, session)

    def test_create_session_creates_valid_session(self):
        """ Test create_session creates a valid session.
        """
        now = datetime.datetime.now()
        user = self.create_user(normal_user=True, with_cart=True)
        session = self.create_session(valid_session=True, user=user)
        db.session.add(session)
        db.session.commit()
        fetched_session = Session.query.first()
        self.assertIsNotNone(fetched_session)
        self.assertEqual(fetched_session, session)
        self.assertTrue(fetched_session.expires_on > now)


class TestBackendTestCaseCreateUser(BackendTestCase):
    def test_create_user_creates_user(self):
        """ Test that create_user creates a user.
        """
        user = self.create_user()
        user.first_name = 'Jason'
        user.email_address = 's@w.com'
        user.set_password('sdf')
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        self.assertIsNotNone(fetched_user)
        self.assertEqual(user, fetched_user)

    def test_create_user_creates_normal_user(self):
        """ Test that create_user creates a 'normal' user.
            A normal user has a first_name, email_address and password
            pre set for convenience.
        """
        user = self.create_user(normal_user=True)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        self.assertIsNotNone(fetched_user)
        self.assertIsNotNone(fetched_user.email_address)
        self.assertIsNotNone(fetched_user.first_name)
        self.assertIsNotNone(fetched_user.password_hash)

    def test_create_user_creates_valid_session(self):
        """ Test that create_user creates a valid session for created user.
        """
        now = datetime.datetime.now()
        user = self.create_user(normal_user=True, valid_session=True)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        fetched_session = Session.query.first()
        self.assertIsNotNone(fetched_session)
        self.assertEqual(fetched_user.sessions, [fetched_session])
        self.assertTrue(fetched_session.expires_on > now)

    def test_create_user_creates_no_session(self):
        """ Test that create_user does not create a session
        by default.
        """
        user = self.create_user(normal_user=True, with_cart=True)
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        fetched_session = Session.query.first()
        self.assertIsNone(fetched_session)
        self.assertEqual(fetched_user.sessions, [])

    def test_create_user_creates_cart(self):
        """ Test that create_user creates a cart for created user.
        """
        user = self.create_user(
            normal_user=True,
            valid_session=True,
            with_cart=True,
        )
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        fetched_cart = Cart.query.first()
        self.assertIsNotNone(fetched_cart)
        self.assertEqual(fetched_user.cart, fetched_cart)
