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

    def test_post(self):
        user = factories.UserFactory()
        db.session.add(user)
        db.session.commit()
        data = dict(
            user_id=user.id,
        )
        response = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(response.status_code, 200, response.json)
        fetched_forgot_password_token = ForgotPasswordToken.query.one()
        self.assertEqual(fetched_forgot_password_token.user, user, response.json)
        self.assertTrue(fetched_forgot_password_token.is_valid())
