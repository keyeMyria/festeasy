from flask_restful import Resource
from flask import request

from backend import db
from backend.models import Cart
from backend.api.utils import get_or_404
from backend.api.v1.schemas import CartSchema
from backend.api.v1.authentication import requires_auth


cart_schema = CartSchema()


class CartSingleton(Resource):
    method_decorators = [requires_auth]

    def get(self, cart_id, authenticated_user):
        cart = get_or_404(Cart, Cart.id == cart_id)
        return cart_schema.dump(cart).data

    def patch(self, cart_id, authenticated_user):
        load_data = cart_schema.load(request.get_json()).data
        cart = get_or_404(Cart, Cart.id == cart_id)
        for arg in load_data:
            setattr(cart, arg, load_data[arg])
        db.session.add(cart)
        db.session.commit()
        return cart_schema.dump(cart).data
