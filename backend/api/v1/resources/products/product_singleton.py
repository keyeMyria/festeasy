from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Product
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import ProductSchema


class ProductSingleton(Resource):
    def get(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        return marshal_or_fail('dump', product, ProductSchema())

    def patch(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        load_data = marshal_or_fail('load', request.get_json(), ProductSchema())
        print(load_data)
        for key, val in load_data.items():
            setattr(product, key, val)
        db.session.add(product)
        db.session.commit()
        return marshal_or_fail('dump', product, ProductSchema())
