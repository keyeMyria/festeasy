from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User, Cart
from backend.api.v1.schemas import UserSchema


user_schema = UserSchema()


class UserCollection(Resource):
    def get(self):
        users = User.query.all()
        return user_schema.dump(users, many=True).data

    def post(self):
        data = user_schema.load(request.get_json()).data
        user = User(**data)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user).data
