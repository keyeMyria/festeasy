from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import User, Cart
from backend.api.utils import get_or_404


resource_fields = {
    'id': fields.Integer,
    'event_id': fields.Integer,
}

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('event_id', type=int)

class CartSingleton(Resource):
    @marshal_with(resource_fields)
    def get(self, cart_id):
        cart = get_or_404(Cart, Cart.id == cart_id)
        return cart

    @marshal_with(resource_fields)
    def patch(self, cart_id):
        args = patch_parser.parse_args(strict=True)
        cart = get_or_404(Cart, Cart.id == cart_id)
        for arg in args:
            setattr(cart, arg, args[arg])
        db.session.add(cart)
        db.session.commit()
        return cart
