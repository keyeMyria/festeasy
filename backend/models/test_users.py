import datetime

from backend import db
from backend.models import User, Session
from backend.utils import ModelTestCase


class TestUser(ModelTestCase):
    def test_create_user(self):
        """ Test that a user can be created.
        """
        user = User(email_address='test@festeasy.co.za')
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

        user = User(email_address='test@festeasy.co.za')
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
