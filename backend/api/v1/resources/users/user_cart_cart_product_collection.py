from flask_restful import Resource

from backend.api.v1.schemas import CartProductSchema
from backend.models import User, CartProduct, Cart


class UserCartCartProductCollection(Resource):
    def __init__(self):
        self.cart_product_schema = CartProductSchema()

    def get(self, user_id):
        # TODO: Play with this query
        cart_products = (CartProduct.query.join(Cart).join(User)
                        .filter(User.id == user_id)
                        .all())
        data, errors = self.cart_product_schema.dump(cart_products, many=True)
        return data
