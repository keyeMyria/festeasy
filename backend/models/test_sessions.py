import datetime

from backend import db
from backend.models import Session, User
from backend.utils import ModelTestCase


class TestSession(ModelTestCase):
    def test_create_session(self):
        """ Test that a session can be created.
        """
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)

        session = Session(expires_on=tomorrow)
        db.session.add(session)
        db.session.commit()

        fetched_session = Session.query.one()
        self.assertEqual(fetched_session, session)

    def test_session_user_relationship(self):
        """ Test that a sessions' user can be set.
        """
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)

        session = Session(expires_on=tomorrow)
        user = User(email_address='test@festeasy.co.za')
        session.user = user

        db.session.add(session)
        db.session.commit()

        fetched_session = Session.query.one()
        fetched_user = User.query.one()

        self.assertEqual(fetched_user.sessions[0], fetched_session)

    def test_user_session_removal(self):
        """ Test that deleting a users session does 
        not delete that user.
        """
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)

        user = User(email_address='test@festeasy.co.za')
        session = Session(expires_on=tomorrow)
        user.sessions.append(session)
        db.session.add(user)
        db.session.commit()
        # Test that session is added to user.sessions
        fetched_user = User.query.one()
        self.assertEqual(len(fetched_user.sessions), 1)
        db.session.delete(session)
        db.session.commit()
        fetched_user = User.query.one()
        # Test that session is removed from user.sessions and user
        # remains
        self.assertIsNotNone(fetched_user)
        self.assertEqual(len(fetched_user.sessions), 0) 
