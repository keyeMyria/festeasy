import datetime

from backend import db
from backend.models import Session, User
from backend.utils import ModelTestCase


class TestSession(ModelTestCase):
    def test_create_session(self):
        """ 
        Test that a session can be created.
        Test that a session can only exist for a particular user.
        (ie: Cannot have stray sessions.)
        Test that a sessions user relationship exists.
        """
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)

        user = User(email_address='test@festeasy.co.za')
        session = Session(expires_on=tomorrow, user=user)
        db.session.add(session)
        db.session.commit()

        fetched_session = Session.query.one()
        fetched_user = User.query.one()

        self.assertEqual(fetched_session, session)
        self.assertEqual(fetched_session.user, user)

    def test_session_deletion(self):
        """ Test that deleting a users session does 
        not delete that user.
        """
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)

        user = User(email_address='test@festeasy.co.za')
        session = Session(expires_on=tomorrow, user=user)
        db.session.add(session)
        db.session.commit()
        
        fetched_user = User.query.one()
        self.assertEqual(fetched_user.sessions[0], session)

        db.session.delete(session)
        db.session.commit()

        fetched_user = User.query.one()
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.sessions, list()) 
