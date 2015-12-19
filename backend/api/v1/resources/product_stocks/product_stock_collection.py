from flask import request
from flask_restful import Resource

from backend import db
from backend.models import ProductStock
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import ProductStockSchema


class ProductStockCollection(Resource):
    def get(self):
        q = ProductStock.query
        product_stocks = q.all()
        return marshal_or_fail(
            'dump',
            product_stocks,
            ProductStockSchema(),
            many=True,
        )

    def post(self):
        load_data = marshal_or_fail(
            'load',
            request.get_json(),
            ProductStockSchema(),
        )
        product_stock = ProductStock()
        for key, val in load_data.items():
            setattr(product_stock, key, val)
        db.session.add(product_stock)
        db.session.commit()
        return marshal_or_fail('dump', product_stock, ProductStockSchema())
