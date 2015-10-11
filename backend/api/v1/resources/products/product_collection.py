from flask_restful import Resource

from backend.models import Product
from backend.api.v1.schemas import ProductSchema


class ProductCollection(Resource):
    def __init__(self):
        self.product_schema = ProductSchema()

    def get(self):
        products = Product.query.all()
        data, errors = self.product_schema.dump(products, many=True)
        return data
