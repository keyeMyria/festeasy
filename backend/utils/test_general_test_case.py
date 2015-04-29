from backend.utils import GeneralTestCase

from backend import db
from backend.models import User, Session


class TestApiTestCase(GeneralTestCase):
    def test_create_user_creates_user(self):
        """ Test that create_user creates a user.
        """
        self.assertIsNone(User.query.first())
        user = self.create_user()
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.one(), user) 

    def test_create_user_creates_no_session(self):
        """ Test that create_user does not create a session
        by default.
        """
        self.assertIsNone(Session.query.first())
        user = self.create_user()
        db.session.add(user)
        db.session.commit()

        self.assertIsNone(Session.query.first())

    def test_create_user_creates_valid_session(self):
        """ Test that create_user creates a valid session.
        """
        self.assertIsNone(Session.query.first())
        self.assertIsNone(Session.query.first())
        user = self.create_user(create_valid_session=True)
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.one(), user)
        self.assertEqual(Session.query.one(), user.sessions[0])
