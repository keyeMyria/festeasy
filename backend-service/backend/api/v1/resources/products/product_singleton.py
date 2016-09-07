from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Product
from backend.api.utils import get_or_404
from backend.api.v1.schemas import ProductSchema


product_schema = ProductSchema()


class ProductSingleton(Resource):
    def get(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        return {
            'data': product_schema.dump(product).data,
        }

    def patch(self, product_id):
        product = get_or_404(Product, Product.id == product_id)
        load_data = product_schema.load(request.get_json()).data
        for key, val in load_data.items():
            setattr(product, key, val)
        db.session.add(product)
        db.session.commit()
        return {
            'data': product_schema.dump(product).data,
        }
