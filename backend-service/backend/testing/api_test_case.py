import json

from backend.testing import BackendTestCase


class APITestCase(BackendTestCase):
    def api_request(
            self,
            method,
            url,
            data=None,
            session_token=None
            ):
        f = getattr(self.client, method)
        kwargs = {}
        headers = {}
        if session_token:
            headers['Authorization'] = session_token
        args = [url]
        kwargs['headers'] = headers
        if data:
            kwargs['data'] = json.dumps(data)
            kwargs['content_type'] = 'application/json'
        return f(*args, **kwargs)
