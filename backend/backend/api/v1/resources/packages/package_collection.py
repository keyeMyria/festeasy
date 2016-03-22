from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Package
from backend.api.v1.schemas import PackageSchema


package_schema = PackageSchema()


# TODO: Needs testing.
def filter_orders(q, order_id):
    q = q.filter(Package.order_id == order_id)
    return q


class PackageCollection(Resource):
    def get(self):
        q = Package.query
        order_id = request.args.get('order-id')
        if order_id:
            q = filter_orders(q, order_id)
        return package_schema.dump(q.all(), many=True).data

    def post(self):
        load_data = package_schema.load(request.get_json()).data
        package = Package(**load_data)
        db.session.add(package)
        db.session.commit()
        return package_schema.dump(package).data
