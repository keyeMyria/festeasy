from flask import request
from flask_restful import Resource

from backend import db
from backend.models import CartProduct
from backend.api.v1.schemas import CartProductSchema


cart_product_schema = CartProductSchema()


class CartProductCollection(Resource):
    def get(self):
        cart_products = CartProduct.query.all()
        return cart_product_schema.dump(cart_products, many=True).data

    def post(self):
        data = CartProductSchema().load(request.get_json()).data
        existing_cart_product = (CartProduct.query.filter(
            CartProduct.cart_id == data['cart_id'],
            CartProduct.product_id == data['product_id'],
        ).one_or_none())
        if existing_cart_product:
            return dict(message='CartProduct already exists.'), 409
        cart_product = CartProduct(**data)
        db.session.add(cart_product)
        db.session.commit()
        return CartProductSchema().dump(cart_product).data
