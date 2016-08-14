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


def filter_available(q, available):
    if available:
        q = q.outerjoin(PackagedStockUnit)
        q = q.filter(PackagedStockUnit.stock_unit_id == None)
    else:
        q = q.join(PackagedStockUnit)
    return q


class StockUnitCollection(Resource):
    def get(self):
        q = StockUnit.query
        available = request.args.get('available')
        if available == 'true':
            q = filter_available(q, True)
        if available == 'false':
            q = filter_available(q, False)
        product_id = request.args.get('product-id')
        if product_id:
            q = filter_product_id(q, product_id)
        product_stocks = q.all()
        return stock_unit_schema.dump(product_stocks, many=True).data

    def post(self):
        many = True if type(request.get_json()) == list else False
        load_data = StockUnitSchema(many=many).load(request.get_json()).data
        stock_units = ([StockUnit(**data) for data in load_data]
                       if many else [StockUnit(**load_data)])
        db.session.add_all(stock_units)
        db.session.commit()
        result = stock_units if many else stock_units[0]
        return StockUnitSchema(many=many).dump(result).data
