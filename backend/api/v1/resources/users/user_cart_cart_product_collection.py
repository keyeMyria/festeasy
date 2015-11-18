from flask import request
from flask_restful import Resource

from backend import db
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
        load_data = marshal_or_fail('load', request.get_json(),
            CartProductSchema())
        cart_product = CartProduct(**load_data)
        db.session.add(cart_product)
        db.session.commit()
        return marshal_or_fail('dump', cart_product, CartProductSchema())
