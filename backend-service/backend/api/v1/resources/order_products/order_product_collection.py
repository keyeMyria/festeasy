from flask import request
from flask_restful import Resource

from backend.models import OrderProduct, Festival, Order
from backend.api.v1.schemas import OrderProductSchema
from backend.api.v1.authentication import requires_auth


order_product_schema = OrderProductSchema()


# TODO: Needs testing.
def filter_order(q, order_id):
    q = q.filter(OrderProduct.order_id == order_id)
    return q


# TODO: Needs testing.
def filter_festival(q, festival_id):
    if festival_id:
        q = q.join(Order)
        q = q.join(Festival)
        q = q.filter(Festival.id == festival_id)
    return q


class OrderProductCollection(Resource):
    method_decorators = [requires_auth]

    def get(self, authenticated_user):
        q = OrderProduct.query
        festival_id = request.args.get('festival-id')
        if festival_id:
            q = filter_festival(q, festival_id)
        order_id = request.args.get('order-id')
        if order_id:
            q = filter_order(q, order_id)
        order_products = q.all()
        return order_product_schema.dump(order_products, many=True).data
