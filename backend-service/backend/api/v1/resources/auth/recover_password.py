from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User, ForgotPasswordToken
from backend.api.v1.schemas import RecoverPasswordSchema
from backend.api.utils import get_or_404
from backend.tasks import send_templated_email


# TODO: Test.
class RecoverPassword(Resource):
    def post(self):
        data = RecoverPasswordSchema().load(request.get_json()).data
        user = get_or_404(User, User.email_address == data['email_address'])
        forgot_password_token = ForgotPasswordToken.create_for_user(user)
        db.session.add(forgot_password_token)
        db.session.commit()
        host_url = (request.environ['HTTP_ORIGIN']
                    if 'HTTP_ORIGIN' in request.environ.keys() else None)
        url = (
            '{host_url}/reset-password?token={token}'
            .format(
                host_url=host_url,
                token=forgot_password_token.token,
            )
        )
        send_templated_email(
            user.email_address,
            'Forgot Password',
            'forgot-password.html',
            data=dict(
                first_name=user.first_name,
                url=url,
            ),
        )
        return "Ok"
