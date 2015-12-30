import logging
import datetime
from flask_restful import Resource
from flask import request

from backend import db
from backend.models import ForgotPasswordToken
from backend.api.utils import get_or_404
from backend.exceptions import APIException
from backend.api.v1.schemas import ResetPasswordSchema


logger = logging.getLogger(__name__)
reset_password_schema = ResetPasswordSchema()


class ResetPassword(Resource):
    # TODO: Invalidate all current sessions
    def post(self):
        now = datetime.datetime.now()
        load_data = reset_password_schema.load(request.get_json()).data
        token = load_data['token']
        password = load_data['password']
        forgot_password_token = get_or_404(
            ForgotPasswordToken,
            ForgotPasswordToken.token == token,
        )
        if not forgot_password_token.is_valid():
            raise APIException(
                status_code=400,
                message='Invalid or expired token.'
            )
        forgot_password_token.used_on = now
        user = forgot_password_token.user
        user.set_password(password)
        db.session.add(forgot_password_token)
        db.session.add(user)
        db.session.commit()
        return
