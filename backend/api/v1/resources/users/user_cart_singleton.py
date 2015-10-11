from flask_restful import Resource

from backend.models import Cart, User
from backend.api.utils import get_or_404
from backend.api.v1.schemas import CartSchema


class UserCartSingleton(Resource):
    def __init__(self):
        self.cart_schema = CartSchema()

    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        cart = user.cart
        if not cart:
            raise Exception('Cart not found.')
        data, errors = self.cart_schema.dump(cart)
        return data
