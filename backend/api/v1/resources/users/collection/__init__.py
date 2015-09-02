from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User, Cart
from backend.api.v1.schemas import UserSchema


class UserCollection(Resource):
    def __init__(self):
        self.user_schema = UserSchema()

    def get(self):
        users = User.query.all()
        data, errors = self.user_schema.dump(users, many=True)
        return data

    def post(self):
        load_data, load_errors = self.user_schema.load(request.get_json())
        user = User(**load_data)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        data, errors = self.user_schema.dump(user)
        return data
