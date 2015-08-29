from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import User, Cart
from backend.api.utils import get_or_404


resource_fields = {
    'id': fields.Integer,
}

parser = reqparse.RequestParser()
parser.add_argument('user_id', location=['view_args'])

class CartResource(Resource):
    @marshal_with(resource_fields)
    def get(self, cart_id, **kwargs):
        args = parser.parse_args()
        user_id = args['user_id']
        if user_id:
            user = get_or_404(User, User.id == user_id)
            assert user.cart_id == cart_id
        cart = get_or_404(Cart, Cart.id == cart_id)
        return cart
