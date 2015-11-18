from flask_restful import Resource

from backend.models import Product
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import ProductSchema


class ProductCollection(Resource):
    def get(self):
        products = Product.query.all()
        return marshal_or_fail('dump', products, ProductSchema(), many=True)
