import datetime

from backend import db
from backend.models import Session, User
from backend.utils import ModelTestCase


class TestSession(ModelTestCase):
    def test_create_session_creates_session(self):
        """ Test that a session can be created for one user.
        Test that a session can only exist for a particular user.
        (ie: Cannot have stray sessions.)
        Test that a sessions user relationship exists.
        """

        user = self.create_user()
        session = self.create_session(create_valid_session=True, user=user)
        db.session.add(session)
        db.session.commit()

        fetched_sessions = Session.query.all()
        self.assertEqual(len(fetched_sessions), 1)
        self.assertEqual(fetched_sessions[0], session)

    def test_session_deletion_keeps_user(self):
        """ Test deleting a users session keeps user
        """

        user = self.create_user()
        session = self.create_session(create_valid_session=True, user=user)
        db.session.add(session)
        db.session.commit()
        
        fetched_sessions = Session.query.all()
        self.assertEqual(len(fetched_sessions), 1)
        self.assertEqual(fetched_sessions[0].user, user)

        db.session.delete(session)
        db.session.commit()

        fetched_users = User.query.all()
        fetched_sessions = Session.query.all()

        self.assertEqual(fetched_sessions, list())
        self.assertEqual(len(fetched_users), 1)
        self.assertEqual(fetched_users[0], user)
        self.assertEqual(fetched_users[0].sessions, list()) 
