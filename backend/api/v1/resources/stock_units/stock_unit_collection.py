from flask import request
from flask_restful import Resource

from backend import db
from backend.models import StockUnit, Product, PackagedStockUnit
from backend.api.v1.schemas import StockUnitSchema


stock_unit_schema = StockUnitSchema()


def filter_product_id(q, product_id):
    q = q.join(Product)
    q = q.filter(Product.id == product_id)
    return q


def filter_availiable(q, availiable):
    if availiable:
        q = q.outerjoin(PackagedStockUnit)
        q = q.filter(PackagedStockUnit.stock_unit_id == None)
    else:
        q = q.join(PackagedStockUnit)
    return q


class StockUnitCollection(Resource):
    def get(self):
        q = StockUnit.query
        availiable = request.args.get('availiable')
        if availiable == 'true':
            q = filter_availiable(q, True)
        if availiable == 'false':
            q = filter_availiable(q, False)
        product_id = request.args.get('product-id')
        if product_id:
            q = filter_product_id(q, product_id)
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
