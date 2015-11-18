from flask_restful import Resource

from backend.models import Product
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import ProductSchema


class ProductSingleton(Resource):
    def get(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        return marshal_or_fail('dump', product, ProductSchema())
