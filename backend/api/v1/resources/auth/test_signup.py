from flask import url_for, current_app

from backend.models import User, Session
from backend.testing import APITestCase


endpoint = 'v1.signup'


class TestSignup(APITestCase):
    def test_post(self):
        email_address = 'asd@fmai.com'
        password = '123'
        first_name = 'Juan'

        response = self.api_request(
            'post',
            url_for(endpoint),
            data=dict(
                email_address=email_address,
                password=password,
                first_name=first_name,
            )
        )

        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], 1, response.json)
        fetched_user = User.query.first()
        fetched_session = Session.query.first()
        self.assertEqual(fetched_user.email_address, email_address, response.json)
        self.assertTrue(fetched_user.has_password(password), response.json)
        self.assertIsNotNone(fetched_session, response.json)
        with open(current_app.config['FILE_EMAILER_PATH']) as f:
            self.assertTrue(f, f.readlines())
