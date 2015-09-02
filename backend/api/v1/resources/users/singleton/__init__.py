from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User
from backend.api.utils import get_or_404
from backend.api.v1.schemas import UserSchema


class UserSingleton(Resource):
    def __init__(self):
        self.user_schema = UserSchema()

    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        data, errors = self.user_schema.dump(user)
        return data

    def patch(self, user_id):
        user = get_or_404(User, User.id == user_id)
        load_data, load_errors = self.user_schema.load(request.get_json())
        for arg in load_data:
            setattr(user, arg, load_data[arg])
        db.session.add(user)
        db.session.commit()
        data, errors = self.user_schema.dump(user)
        return data
