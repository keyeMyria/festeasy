from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User, Cart
from backend.api.v1.schemas import UserSchema
from backend.api.v1.authentication import requires_auth


user_schema = UserSchema()


class UserCollection(Resource):
    method_decorators = [requires_auth]

    def get(self, authenticated_user):
        users = User.query.all()
        return user_schema.dump(users, many=True).data

    def post(self, authenticated_user):
        data = user_schema.load(request.get_json()).data
        user = User(**data)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user).data
