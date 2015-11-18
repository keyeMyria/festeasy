from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import UserSchema


class UserSingleton(Resource):
    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        return marshal_or_fail('dump', user, UserSchema())

    def patch(self, user_id):
        user = get_or_404(User, User.id == user_id)
        load_data = marshal_or_fail('load', request.get_json(), UserSchema())
        for arg in load_data:
            setattr(user, arg, load_data[arg])
        db.session.add(user)
        db.session.commit()
        return marshal_or_fail('dump', user, UserSchema())
