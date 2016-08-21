import logging
from flask_restful import Resource
from flask import request

from backend import db
from backend.models import User
from backend.api.utils import get_or_404
from backend.exceptions import APIException
from backend.api.v1.schemas import ChangePasswordSchema
from backend.api.v1.authentication import requires_auth


logger = logging.getLogger(__name__)
change_password_schema = ChangePasswordSchema()


class ChangePassword(Resource):
    method_decorators = [requires_auth]

    def post(self, user_id, authenticated_user):
        load_data = change_password_schema.load(request.get_json()).data
        current_password = load_data['current_password']
        new_password = load_data['new_password']
        user = get_or_404(User, User.id == user_id)
        if not user.has_password(current_password):
            logger.error('Incorrect current password.')
            raise APIException(
                status_code=400,
                message='Incorrect password.',
            )
        user.set_password(new_password)
        db.session.add(user)
        db.session.commit()
        return
