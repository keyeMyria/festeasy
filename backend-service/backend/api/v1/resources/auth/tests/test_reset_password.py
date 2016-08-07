import datetime
from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import ForgotPasswordToken, User


endpoint = 'v1.resetpassword'


class TestResetPassword(APITestCase):
    def test_correct_token(self):
        new_password = '123321'
        user = factories.UserFactory()
        fpt = ForgotPasswordToken.create_for_user(user)
        db.session.add(fpt)
        db.session.add(user)
        db.session.commit()
        data = dict(
            token=fpt.token,
            password=new_password,
        )
        response = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(response.status_code, 200, response.json)
        fetched_user = User.query.one()
        self.assertTrue(fetched_user.has_password(new_password))
        self.assertFalse(fpt.is_valid())

    def test_incorrect_token(self):
        new_password = '123321'
        user = factories.UserFactory()
        fpt = ForgotPasswordToken.create_for_user(user)
        db.session.add(fpt)
        db.session.add(user)
        db.session.commit()
        data = dict(
            token=fpt.token + 'wrong',
            password=new_password,
        )
        response = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(response.status_code, 404, response.json)

    def test_invalid_token(self):
        now = datetime.datetime.now()
        new_password = '123321'
        user = factories.UserFactory()
        fpt = ForgotPasswordToken.create_for_user(user)
        fpt.used_on = now
        db.session.add(fpt)
        db.session.add(user)
        db.session.commit()
        data = dict(
            token=fpt.token,
            password=new_password,
        )
        response = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(response.status_code, 400, response.json)
        self.assertFalse(user.has_password(new_password))
