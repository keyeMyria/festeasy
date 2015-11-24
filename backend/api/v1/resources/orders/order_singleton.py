from flask_restful import Resource

from backend.models import Order
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import OrderSchema


class OrderSingleton(Resource):
    def get(self, order_id):
        order = get_or_404(Order, Order.id == order_id)
        return marshal_or_fail('dump', order, OrderSchema())
