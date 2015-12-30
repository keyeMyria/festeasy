from factory import Factory

from backend.models import ForgotPasswordToken


class ForgotPasswordTokenFactory(Factory):
    class Meta:
        model = ForgotPasswordToken
