from flask_restful import Resource

from backend.models import User
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import CartSchema


class UserCartSingleton(Resource):
    def get(self, user_id):
        user = get_or_404(User, User.id == user_id)
        cart = user.cart
        if not cart:
            raise Exception('Cart not found.')
        return marshal_or_fail('dump', cart, CartSchema())
