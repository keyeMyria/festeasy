from flask_restful import Resource

from backend.models import CartProduct
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import CartProductSchema


class CartProductCollection(Resource):
    def __init__(self):
        self.cart_product_schema = CartProductSchema()

    def get(self):
        cart_products = CartProduct.query.all()
        return marshal_or_fail(
            'dump', cart_products, CartProductSchema(), many=True)
