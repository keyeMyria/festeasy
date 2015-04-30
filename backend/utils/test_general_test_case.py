import datetime

from backend import db
from backend.utils import GeneralTestCase, random_string
from backend.models import User, Session


class TestGeneralTestCaseCreateSession(GeneralTestCase):
    def test_create_session_creates_session(self):
        """ Test create_session creates a session.
        """
        self.assertIsNone(Session.query.first())

        now = datetime.datetime.now()
        expires_on = now + datetime.timedelta(seconds=30)
        token = random_string(25)
        user = self.create_user()

        session = self.create_session(expires_on=expires_on, token=token, for_user=user)

        db.session.add(session)
        db.session.commit()

        self.assertEqual(Session.query.one(), session)


class TestGeneralTestCaseCreateUser(GeneralTestCase):
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
        """ Test that create_user creates a valid session for created user.
        """
        self.assertIsNone(Session.query.first())

        user = self.create_user(create_valid_session=True)
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.one(), user)
        self.assertEqual(Session.query.one(), user.sessions[0])
