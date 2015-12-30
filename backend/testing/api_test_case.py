import json
from base64 import b64encode

from backend.testing import BackendTestCase
from .layers import APILayer


class APITestCase(BackendTestCase):
    layer = APILayer

    def api_request(self, method,
                    url, data=None, as_user=None, with_session=None):
        kwargs = dict()
        headers = dict()

        if as_user:
            if with_session:
                session_token = with_session.token
                a = b64encode(
                    bytes('api:{0}'.format(session_token), 'utf-8')
                ).decode('utf-8')
                headers['Authorization'] = 'xBasic {0}'.format(a)

        f = getattr(self.client, method)
        args = [url]

        kwargs['headers'] = headers

        if data:
            kwargs['data'] = json.dumps(data)
            kwargs['content_type'] = 'application/json'
        return f(*args, **kwargs)
