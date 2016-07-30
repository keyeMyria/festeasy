from flask_restful import Resource
from flask import request

from backend import db
from backend.models import Cart
from backend.api.utils import get_or_404
from backend.api.v1.schemas import CartSchema


cart_schema = CartSchema()


class CartSingleton(Resource):
    def get(self, cart_id):
        cart = get_or_404(Cart, Cart.id == cart_id)
        return cart_schema.dump(cart).data

    def patch(self, cart_id):
        load_data = cart_schema.load(request.get_json()).data
        cart = get_or_404(Cart, Cart.id == cart_id)
        for arg in load_data:
            setattr(cart, arg, load_data[arg])
        db.session.add(cart)
        db.session.commit()
        return cart_schema.dump(cart).data
