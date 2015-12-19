from flask import request
from flask_restful import Resource

from backend import db
from backend.models import ProductStock
from backend.api.v1.schemas import ProductStockSchema


product_stock_schema = ProductStockSchema()


class ProductStockCollection(Resource):
    def get(self):
        q = ProductStock.query
        product_stocks = q.all()
        return product_stock_schema.dump(product_stocks, many=True).data

    def post(self):
        load_data = product_stock_schema.load(request.get_json()).data
        product_stock = ProductStock()
        for key, val in load_data.items():
            setattr(product_stock, key, val)
        db.session.add(product_stock)
        db.session.commit()
        return product_stock_schema.dump(product_stock).data
