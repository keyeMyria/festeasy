import datetime

from backend import db
from backend.testing import GeneralTestCase
from backend.utils import random_string
from backend.models import User, Session, Cart


class TestGeneralTestCaseCreateSession(GeneralTestCase):
    def test_create_session_creates_session(self):
        """ Test create_session creates a session.
        """
        now = datetime.datetime.now()
        expires_on = now + datetime.timedelta(seconds=30)
        token = random_string(25)
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        session = self.create_session(expires_on=expires_on, token=token, user=user)
        db.session.add(session)
        db.session.commit()
        fetched_session = Session.query.first()
        self.assertIsNotNone(fetched_session)
        self.assertEqual(fetched_session, session)

    def test_create_session_creates_valid_session(self):
        """ Test create_session creates a valid session.
        """
        now = datetime.datetime.now()
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        session = self.create_session(create_valid_session=True, user=user)
        db.session.add(session)
        db.session.commit()
        fetched_session = Session.query.first()
        self.assertIsNotNone(fetched_session)
        self.assertEqual(fetched_session, session)
        self.assertTrue(fetched_session.expires_on > now)

class TestGeneralTestCaseCreateUser(GeneralTestCase):
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
        user = self.create_user(create_normal_user=True)
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
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        fetched_session = Session.query.first()
        self.assertIsNotNone(fetched_session)
        self.assertEqual(fetched_user.sessions, [fetched_session])

    def test_create_user_creates_no_session(self):
        """ Test that create_user does not create a session
        by default.
        """
        user = self.create_user(create_normal_user=True, create_valid_cart=True)
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        fetched_session = Session.query.first()
        self.assertIsNone(fetched_session)
        self.assertEqual(fetched_user.sessions, [])

    def test_create_user_creates_valid_cart(self):
        """ Test that create_user creates a valid cart for created user.
        """
        user = self.create_user(
            create_normal_user=True, 
            create_valid_session=True, 
            create_valid_cart=True,
        )
        db.session.add(user)
        db.session.commit()
        fetched_user = User.query.first()
        fetched_cart = Cart.query.first()
        self.assertIsNotNone(fetched_cart)
        self.assertEqual(fetched_user.cart, fetched_cart)
