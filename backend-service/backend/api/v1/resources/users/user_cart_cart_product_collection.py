from flask import request
from flask_restful import Resource

from backend import db
from backend.api.v1.schemas import CartProductSchema
from backend.models import User, CartProduct, Cart


cart_product_schema = CartProductSchema()


class UserCartCartProductCollection(Resource):
    def get(self, user_id):
        # TODO: Play with this query
        cart_products = (CartProduct.query.join(Cart).join(User)
                        .filter(User.id == user_id)
                        .all())
        return cart_product_schema.dump(cart_products, many=True).data

    def post(self, user_id):
        load_data = cart_product_schema.load(request.get_json()).data
        existing_cart_product = (CartProduct.query
            .filter(CartProduct.product_id == load_data['product_id'])
            .filter(CartProduct.cart_id == load_data['cart_id'])
            .first())
        if existing_cart_product:
            return dict(message='CartProduct already exists.'), 409
        cart_product = CartProduct(**load_data)
        db.session.add(cart_product)
        db.session.commit()
        return cart_product_schema.dump(cart_product).data
