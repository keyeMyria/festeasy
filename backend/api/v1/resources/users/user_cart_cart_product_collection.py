from flask_restful import Resource

from backend.api.v1.schemas import CartProductSchema
from backend.api.utils import marshal_or_fail
from backend.models import User, CartProduct, Cart


class UserCartCartProductCollection(Resource):
    def get(self, user_id):
        # TODO: Play with this query
        cart_products = (CartProduct.query.join(Cart).join(User)
                        .filter(User.id == user_id)
                        .all())
        return marshal_or_fail('dump', cart_products,
            CartProductSchema(), many=True)

    def post(self, user_id):
        pass
