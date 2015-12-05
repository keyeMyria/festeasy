from flask import request
from flask_restful import Resource

from backend.models import Product, Category, ProductCategory
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import ProductSchema


class ProductCollection(Resource):
    def get(self):
        category = request.args.get('category')
        q = Product.query
        if category:
            q = q.join(ProductCategory)
            q = q.join(Category)
            q = q.filter(Category.name == category)
        products = q.all()
        return marshal_or_fail('dump', products, ProductSchema(), many=True)
