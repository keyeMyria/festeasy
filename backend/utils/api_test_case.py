from base64 import b64encode
import datetime
import json

from backend import create_app, db
from backend.utils import GeneralTestCase
from backend.utils.random_string import random_string
from backend.models import User, Session


class APITestCase(GeneralTestCase):

    def api_request(self, method, url, data=None, as_user=None, with_session=None):
        kwargs = dict()
        headers = dict()

        if as_user:
            if with_session:
                session_token = with_session.token
                a = b64encode(bytes('api:{0}'.format(session_token), 'utf-8')).decode('utf-8')
                headers['Authorization'] = 'xBasic {0}'.format(a)

        f = getattr(self.client, method)
        args = [url]

        kwargs['headers'] = headers

        if data:
            kwargs['data'] = json.dumps(data)
            kwargs['content_type'] = 'application/json'
         
        return f(*args, **kwargs)
