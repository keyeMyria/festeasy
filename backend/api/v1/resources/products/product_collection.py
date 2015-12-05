from flask import request
from flask_restful import Resource

from backend.models import Product, Category
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import ProductSchema


class ProductCollection(Resource):
    def get(self):
        category = request.args.get('category')
        if category:
            c = Category.query.filter(Category.name == category).first()
            if c:
                products = c.products
            else:
                products = []
        else:
            products = Product.query.all()
        return marshal_or_fail('dump', products, ProductSchema(), many=True)
