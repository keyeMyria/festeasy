import datetime

from backend import db
from backend.testing import factories
from backend.testing import ModelTestCase

from . import ForgotPasswordToken


class TestForgotPasswordToken(ModelTestCase):
    def test_create_for_user(self):
        """ Test that ForgotPasswordToken.create_for_user creates a valid token
        for given user.
        """
        user = factories.UserFactory()
        forgot_password_token = ForgotPasswordToken.create_for_user(user)
        db.session.add(forgot_password_token)
        db.session.commit()
        self.assertTrue(forgot_password_token.is_valid())

    def test_is_valid(self):
        now = datetime.datetime.now()
        past_date = now - datetime.timedelta(seconds=10)
        future_date = now + datetime.timedelta(seconds=10)

        user = factories.UserFactory()
        forgot_password_token = factories.ForgotPasswordTokenFactory()
        forgot_password_token.user = user
        forgot_password_token.token = ForgotPasswordToken.get_token()

        forgot_password_token.expires_on = future_date
        forgot_password_token.used_on = None
        db.session.add(forgot_password_token)
        db.session.commit()
        self.assertTrue(forgot_password_token.is_valid())

        forgot_password_token.used_on = now
        db.session.add(forgot_password_token)
        db.session.commit()
        self.assertFalse(forgot_password_token.is_valid())

        forgot_password_token.used_on = None
        forgot_password_token.expires_on = past_date
        db.session.add(forgot_password_token)
        db.session.commit()
        self.assertFalse(forgot_password_token.is_valid())
