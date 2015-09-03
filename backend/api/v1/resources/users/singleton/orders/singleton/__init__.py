from flask_restful import Resource

from backend.models import Order
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderSchema


class UserOrderSingleton(Resource):
    def __init__(self):
        self.order_schema = OrderSchema()

    def get(self, user_id, order_id):
        order = get_or_404(Order, Order.id == order_id)
        assert(order.user_id == user_id)
        data, errors = self.order_schema.dump(order)
        return data
