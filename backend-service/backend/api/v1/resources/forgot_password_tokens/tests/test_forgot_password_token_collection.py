from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import ForgotPasswordToken


endpoint = 'v1.forgotpasswordtokencollection'


class TestForgotPasswordTokenCollection(APITestCase):
    def test_get(self):
        user = factories.UserFactory()
        forgot_password_token = ForgotPasswordToken.create_for_user(user)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(
            response.json[0]['token'],
            forgot_password_token.token,
            response.json,
        )
