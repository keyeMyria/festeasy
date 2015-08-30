from flask_restful import Resource, fields, marshal_with

from backend.models import Order
from backend.api.utils import get_or_404


singleton_fields = {
    'id': fields.Integer,
}


class OrderSingleton(Resource):
    @marshal_with(singleton_fields)
    def get(self, order_id):
        order = get_or_404(Order, Order.id == order_id)
        return order
