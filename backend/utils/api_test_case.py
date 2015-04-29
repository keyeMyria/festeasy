import datetime
from flask.ext.testing import TestCase

from backend import create_app, db
from backend.utils.random_string import random_string
from backend.models import User, Session


class APITestCase(TestCase):
    def create_app(self):
        app = create_app(config='testing')
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_user(self, email_address='user@APITestCase.takenote', 
        password='test_password', create_valid_session=False):
        now = datetime.datetime.now()
        user = User(email_address=email_address, password=password)
        if create_valid_session:
            expires_on = now + datetime.timedelta(seconds=30)
            token = random_string(25)
            session = Session(expires_on=expires_on, token=token)
            user.sessions.append(session)
        return user

    def api_request(self, method, url, data=None, as_user=None, with_session=None):
        kwargs = dict()

        if as_user:
            if with_session:
                session_token = with_session.token
            auth_headers = {'Authorization': 'xBasic %s' % ('api:%s' % session_token).encode('base64')[:-1]}
            kwargs = {'headers': auth_headers}

        f = getattr(self.client, method)
        args = [url]

        if data:
            kwargs['data'] = json.dumps(data)
            kwargs['content_type'] = 'application/json'

        return f(*args, **kwargs)
