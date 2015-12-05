from flask import request
from flask_restful import Resource

from backend.models import Product, Category, ProductCategory
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import ProductSchema


def filter_categories(q):
    category = request.args.get('category')
    if category:
        q = q.join(ProductCategory)
        q = q.join(Category)
        q = q.filter(Category.name == category)
    return q


class ProductCollection(Resource):
    def get(self):
        q = Product.query
        q = filter_categories(q)
        products = q.all()
        return marshal_or_fail('dump', products, ProductSchema(), many=True)
