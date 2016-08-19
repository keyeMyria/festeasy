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
