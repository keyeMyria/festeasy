from flask import url_for

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

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['user']['email_address'], email_address)
        self.assertEqual(response.json['session']['id'], 1)
        fetched_user = User.query.first()
        fetched_session = Session.query.first()
        self.assertEqual(fetched_user.email_address, email_address)
        self.assertTrue(fetched_user.has_password(password))
        self.assertIsNotNone(fetched_session)
