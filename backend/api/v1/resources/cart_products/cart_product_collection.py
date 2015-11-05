from flask import request
from flask_restful import Resource

from backend import db
from backend.models import CartProduct
from backend.api.v1.schemas import CartProductSchema


class CartProductCollection(Resource):
    def __init__(self):
        self.cart_product_schema = CartProductSchema()

    def get(self):
        cart_products = CartProduct.query.all()
        data, errors = self.cart_product_schema.dump(cart_products, many=True)
        return data
