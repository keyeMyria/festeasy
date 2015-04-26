from backend import db
from backend.models import User
from backend.utils import ModelTestCase


class TestUser(ModelTestCase):
	def test_create_user(self):
		user = User(email_address='test@festeasy.co.za')
		db.session.add(user)
		db.session.commit()
