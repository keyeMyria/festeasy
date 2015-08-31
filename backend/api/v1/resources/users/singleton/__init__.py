from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import User
from backend.api.utils import get_or_404


user_fields = {
    'id': fields.Integer,
    'email_address': fields.String,
    'cart_id': fields.Integer,
}


patch_parser = reqparse.RequestParser()
patch_parser.add_argument('first_name', type=str)
patch_parser.add_argument('last_name', type=str)


class UserSingleton(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        return user

    @marshal_with(user_fields)
    def delete(self, user_id):
        user = get_or_404(User, User.id == user_id)
        db.session.delete(user)
        db.session.commit()
        return user

    @marshal_with(user_fields)
    def patch(self, user_id):
        args = patch_parser.parse_args(strict=True)
        user = get_or_404(User, User.id == user_id)
        for arg in args:
            setattr(user, arg, args[arg])
        db.session.add(user)
        db.session.commit()
        return user
