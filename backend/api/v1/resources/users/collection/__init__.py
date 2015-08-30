from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import User, Cart
from backend.api.utils import get_or_404


user_fields = {
    'id': fields.Integer,
    'email_address': fields.String,
    'cart_id': fields.Integer,
}

class UserCollection(Resource):
    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('email_address', type=str, required=True)
        self.post_parser.add_argument('first_name', type=str, required=True)
        self.post_parser.add_argument('password', type=str, required=True)

    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        args = self.post_parser.parse_args(strict=True)
        user = User(**args)
        user.cart = Cart()
        db.session.add(user)
        db.session.commit()
        return user
