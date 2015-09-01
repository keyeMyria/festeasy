from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User
from backend.api.utils import get_or_404
from ..schema import authenticate_and_get_schema


class UserSingleton(Resource):
    def __init__(self):
        self.authenticated_user, self.user_schema = (
            authenticate_and_get_schema(request)
        )

    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        data, errors = self.user_schema.dump(user)
        return data

    def delete(self, user_id):
        user = get_or_404(User, User.id == user_id)
        db.session.delete(user)
        db.session.commit()
        data, errors = self.user_schema.dump(user)
        return data

    def patch(self, user_id):
        user = get_or_404(User, User.id == user_id)
        data, errors = self.user_schema.load(request.get_json())
        for arg in data:
            setattr(user, arg, data[arg])
        db.session.add(user)
        db.session.commit()
        data, errors = self.user_schema.dump(user)
        return data
