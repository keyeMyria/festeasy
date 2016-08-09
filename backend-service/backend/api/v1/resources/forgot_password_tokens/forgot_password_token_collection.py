from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User, ForgotPasswordToken
from backend.api.v1.schemas import ForgotPasswordTokenSchema
from backend.api.utils import get_or_404
from backend.tasks import send_templated_email


forgot_password_token_schema = ForgotPasswordTokenSchema()


def token_filter(token, q):
    q = q.filter_by(token=token)
    return q


class ForgotPasswordTokenCollection(Resource):
    def get(self):
        q = ForgotPasswordToken.query
        token = request.args.get('token')
        if token:
            q = token_filter(token, q)
        forgot_password_tokens = q.all()
        return (forgot_password_token_schema.dump(
                forgot_password_tokens,
                many=True)
                .data)

    def post(self):
        data = forgot_password_token_schema.load(request.get_json()).data
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
