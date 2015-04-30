import datetime

from backend import create_app, db
from backend.utils import GeneralTestCase
from backend.utils.random_string import random_string
from backend.models import User, Session


class APITestCase(GeneralTestCase):

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