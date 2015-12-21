from flask_restful import Resource
from flask import request

from backend import db
from backend.api.utils import get_or_404
from backend.models import CartProduct
from backend.api.v1.schemas import CartProductSchema


cart_product_schema = CartProductSchema()


class CartProductSingleton(Resource):
    def get(self, cart_product_id):
        cart_product = get_or_404(
            CartProduct,
            CartProduct.id == cart_product_id
        )
        return cart_product_schema.dump(cart_product).data

    def patch(self, cart_product_id):
        load_data = cart_product_schema.load(request.get_json()).data
        cart_product = get_or_404(
            CartProduct,
            CartProduct.id == cart_product_id
        )
        for arg in load_data:
            setattr(cart_product, arg, load_data[arg])
        db.session.add(cart_product)
        db.session.commit()
        return cart_product_schema.dump(cart_product).data

    # TODO: Return a copy of the deleted entity.
    def delete(self, cart_product_id):
        cart_product = get_or_404(
            CartProduct,
            CartProduct.id == cart_product_id
        )
        db.session.delete(cart_product)
        db.session.commit()
        return
