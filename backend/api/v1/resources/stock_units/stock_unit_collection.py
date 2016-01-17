from flask import request
from flask_restful import Resource

from backend import db
from backend.models import StockUnit
from backend.api.v1.schemas import StockUnitSchema


stock_unit_schema = StockUnitSchema()


class StockUnitCollection(Resource):
    def get(self):
        q = StockUnit.query
        product_stocks = q.all()
        return stock_unit_schema.dump(product_stocks, many=True).data

    def post(self):
        load_data = stock_unit_schema.load(request.get_json()).data
        product_stock = StockUnit()
        for key, val in load_data.items():
            setattr(product_stock, key, val)
        db.session.add(product_stock)
        db.session.commit()
        return stock_unit_schema.dump(product_stock).data
