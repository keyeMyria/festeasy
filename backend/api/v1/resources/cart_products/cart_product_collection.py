from flask_restful import Resource

from backend.models import CartProduct
from backend.api.v1.schemas import CartProductSchema


cart_product_schema = CartProductSchema()


class CartProductCollection(Resource):
    def get(self):
        cart_products = CartProduct.query.all()
        return cart_product_schema.dump(cart_products, many=True).data
