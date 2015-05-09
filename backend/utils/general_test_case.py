import datetime
from flask.ext.testing import TestCase

from backend import create_app, db
from backend.utils.random_string import random_string
from backend.models import User, Session, Product


class GeneralTestCase(TestCase):
    def create_app(self):
        app = create_app(config='testing')
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_product(self, name=None, price_cents=None):
        product = Product(name=name, price_cents=price_cents)
        return product

    def create_session(self, expires_on=None, token=None, for_user=None, create_valid_session=False):
        now = datetime.datetime.now()
        if create_valid_session:
            expires_on = now + datetime.timedelta(seconds=30)
            token = random_string(25)
        session = Session(expires_on=expires_on, user=for_user, token=token)
        return session

    def create_user(self, email_address='user@GeneralTestCase.takenote', 
        password='test_password', first_name='Johannes', create_valid_session=False):
        now = datetime.datetime.now()
        user = User(email_address=email_address, password=password, first_name=first_name)
        if create_valid_session:
            expires_on = now + datetime.timedelta(seconds=30)
            token = random_string(25)
            session = self.create_session(expires_on=expires_on, token=token)
            user.sessions.append(session)
        return user
