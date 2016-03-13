from flask import request
from flask_restful import Resource

from backend import db
from backend.models import PackagedStockUnit, Package, Order, Festival
from backend.api.v1.schemas import PackagedStockUnitSchema


psu_schema = PackagedStockUnitSchema()


# TODO: Needs testing.
def filter_order_id(q, order_id):
    q = q.join(Package).join(Order)
    q = q.filter(Order.id == order_id)
    return q


# TODO: Needs testing.
def filter_package_id(q, package_id):
    q = q.join(Package)
    q = q.filter(Package.id == package_id)
    return q


def filter_festival_id(q, festival_id):
    q = q.join(Package).join(Order).join(Festival)
    q = q.filter(Festival.id == festival_id)
    return q


class PackagedStockUnitCollection(Resource):
    def get(self):
        q = PackagedStockUnit.query
        festival_id = request.args.get('festival-id')
        if festival_id:
            q = filter_festival_id(q, festival_id)
        package_id = request.args.get('package-id')
        if package_id:
            q = filter_package_id(q, package_id)
        order_id = request.args.get('order-id')
        if order_id:
            q = filter_order_id(q, order_id)
        return psu_schema.dump(q.all(), many=True).data

    def post(self):
        load_data = psu_schema.load(request.get_json()).data
        psu = None
        if load_data:
            psu = PackagedStockUnit(**load_data)
        else:
            psu = PackagedStockUnit()
        db.session.add(psu)
        db.session.commit()
        return psu_schema.dump(psu).data
