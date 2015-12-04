from flask_restful import Resource
from flask import request

from backend.models import User
from backend.api.utils import get_or_404
from backend.api.v1.exceptions import APIException


class ChangePassword(Resource):
    def post(self, user_id):
        current_password = request.get_json()['current_password']
        new_password = request.get_json()['new_password']
        user = get_or_404(User, User.id == user_id)
        if not user.has_password(current_password):
            raise APIException(
                status_code=401,
                message='Incorrect password.',
            )
        user.set_password(new_password)
        return
