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

	def test_user_session(self):
		""" Test that a session can be appended to 
		a users' sessions.
		"""
		now = datetime.datetime.now()
		tomorrow = now + datetime.timedelta(days=1)

		session = Session(expires_on=tomorrow)
		user = User(email_address='test@festeasy.co.za')
		user.sessions.append(session)

		db.session.add(user)
		db.session.commit()

		fetched_user = User.query.one()
		self.assertEqual(len(fetched_user.sessions), 1)

	def test_user_deletion_deletes_sessions(self):
		""" Test that deleting a user also deletes that 
		users sessions."""
		now = datetime.datetime.now()
		tomorrow = now + datetime.timedelta(days=1)

		session = Session(expires_on=tomorrow)
		another_session = Session(expires_on=tomorrow)
		user = User(email_address='test@festeasy.co.za')

		user.sessions.append(session)
		user.sessions.append(another_session)
		db.session.add(user)
		db.session.commit()

		fetched_user = User.query.one()
		# Assert that user has two sessions
		self.assertEqual(len(fetched_user.sessions), 2)
		# Assert that no Sessions remain
		db.session.delete(fetched_user)
		self.assertEqual(len(Session.query.all()), 0)
