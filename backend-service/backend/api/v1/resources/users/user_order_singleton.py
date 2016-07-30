from flask_restful import Resource

from backend.models import Order
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderSchema


order_schema = OrderSchema()


class UserOrderSingleton(Resource):
    def get(self, user_id, order_id):
        order = get_or_404(Order, Order.id == order_id)
        assert(order.user_id == user_id)
        return order_schema.dump(order).data
