from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User, Cart
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import UserSchema


class UserCollection(Resource):
    def __init__(self):
        self.user_schema = UserSchema()

    def get(self):
        users = User.query.all()
        return marshal_or_fail('dump', users, schema=UserSchema, many=True)

    def post(self):
        load_data = marshal_or_fail(
            'load',
            request.get_json(),
            schema=UserSchema,
        )
        user = User(**load_data)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        return marshal_or_fail('dump', user, schema=UserSchema)
