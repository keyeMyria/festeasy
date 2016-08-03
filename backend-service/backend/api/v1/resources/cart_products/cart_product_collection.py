from flask import request
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser

from backend import db
from backend.models import CartProduct
from backend.api.v1.schemas import CartProductSchema


cart_product_schema = CartProductSchema()
query_args = {
    'cart_id': fields.Integer(
        load_from='cart-id',
        missing=None,
    )
}


# TODO: Test.
def cart_id_filter(q, cart_id):
    return q.filter(CartProduct.cart_id == cart_id)


class CartProductCollection(Resource):
    def get(self):
        params = parser.parse(query_args, request)
        cart_id = params['cart_id']
        q = CartProduct.query
        if cart_id:
            q = cart_id_filter(q, cart_id)
        q = q.order_by(CartProduct.created_on.desc())
        return cart_product_schema.dump(q.all(), many=True).data

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
