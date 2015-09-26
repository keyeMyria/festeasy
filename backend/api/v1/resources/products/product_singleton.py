from flask_restful import Resource

from backend.models import Product
from backend.api.utils import get_or_404
from backend.api.v1.schemas import ProductSchema


class ProductSingleton(Resource):
    def __init__(self):
        self.product_schema = ProductSchema()

    def get(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        data, errors = self.product_schema.dump(product)
        return data
