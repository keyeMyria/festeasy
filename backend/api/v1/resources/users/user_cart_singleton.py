from flask import request
from flask_restful import Resource

from backend import db
from backend.models import User
from backend.api.utils import get_or_404
from backend.api.v1.schemas import CartSchema


cart_schema = CartSchema()


class UserCartSingleton(Resource):
    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        cart = user.cart
        if not cart:
            raise Exception('Cart not found.')
        return cart_schema.dump(cart).data

    def patch(self, user_id):
        user = get_or_404(User, User.id == user_id)
        cart = user.cart
        load_data = cart_schema.load(request.get_json()).data
        for key, val in load_data.items():
            setattr(cart, key, val)
        db.session.add(cart)
        db.session.commit()
        return cart_schema.dump(cart).data
