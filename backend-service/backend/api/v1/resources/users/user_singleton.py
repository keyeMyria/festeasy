from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User
from backend.api.utils import get_or_404
from backend.api.v1.schemas import UserSchema
from backend.api.v1.authentication import requires_auth


user_schema = UserSchema()


class UserSingleton(Resource):
    method_decorators = [requires_auth]

    def get(self, user_id, authenticated_user):
        user = get_or_404(User, User.id == user_id)
        return user_schema.dump(user).data

    def patch(self, user_id, authenticated_user):
        user = get_or_404(User, User.id == user_id)
        load_data = user_schema.load(request.get_json()).data
        for arg in load_data:
            setattr(user, arg, load_data[arg])
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user).data
