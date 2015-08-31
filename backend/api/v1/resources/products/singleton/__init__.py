from flask_restful import Resource, fields, marshal_with

from backend.models import Product
from backend.api.utils import get_or_404


singleton_fields = {
    'id': fields.Integer,
}


class ProductSingleton(Resource):
    @marshal_with(singleton_fields)
    def get(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        return product
