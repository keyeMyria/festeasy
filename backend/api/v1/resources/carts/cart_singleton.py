from flask_restful import Resource
from flask import request

from backend import db
from backend.models import Cart
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import CartSchema


class CartSingleton(Resource):
    def __init__(self):
        self.cart_schema = CartSchema()

    def get(self, cart_id):
        cart = get_or_404(Cart, Cart.id == cart_id)
        return marshal_or_fail('dump', cart, CartSchema())

    def patch(self, cart_id):
        load_data = marshal_or_fail('load', request.get_json(), CartSchema())
        cart = get_or_404(Cart, Cart.id == cart_id)
        for arg in load_data:
            setattr(cart, arg, load_data[arg])
        db.session.add(cart)
        db.session.commit()
        return marshal_or_fail('dump', cart, CartSchema())
