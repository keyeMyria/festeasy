from flask_restful import Resource
from flask import request

from backend import db
from backend.api.utils import get_or_404, marshal_or_fail
from backend.models import CartProduct
from backend.api.v1.schemas import CartProductSchema


class CartProductSingleton(Resource):
    def __init__(self):
        self.cart_product_schema = CartProductSchema()

    def get(self, cart_product_id):
        cart_product = get_or_404(
            CartProduct,
            CartProduct.id == cart_product_id
        )
        return marshal_or_fail('dump', cart_product, CartProductSchema())

    def patch(self, cart_product_id):
        load_data = marshal_or_fail('load', request.get_json(), CartProductSchema())
        cart_product = get_or_404(
            CartProduct,
            CartProduct.id == cart_product_id
        )
        for arg in load_data:
            setattr(cart_product, arg, load_data[arg])
        db.session.add(cart_product)
        db.session.commit()
        return marshal_or_fail('dump', cart_product, CartProductSchema())

    def delete(self, cart_product_id):
        cart_product = get_or_404(
            CartProduct,
            CartProduct.id == cart_product_id
        )
        db.session.delete(cart_product)
        db.session.commit()
        return
