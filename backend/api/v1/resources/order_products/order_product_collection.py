from flask import request
from flask_restful import Resource

from backend.models import OrderProduct, Festival, Order
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import OrderProductSchema


def filter_festival(q):
    festival_id = request.args.get('festival-id')
    if festival_id:
        q = q.join(Order)
        q = q.join(Festival)
        q = q.filter(Festival.id == festival_id)
    return q


class OrderProductCollection(Resource):
    def get(self):
        q = OrderProduct.query
        q = filter_festival(q)
        order_products = q.all()
        return marshal_or_fail(
            'dump',
            order_products,
            OrderProductSchema(),
            many=True,
        )
