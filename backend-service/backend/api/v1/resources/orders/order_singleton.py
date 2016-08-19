from flask_restful import Resource

from backend.models import Order
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderSchema

order_schema = OrderSchema()


class OrderSingleton(Resource):
    def get(self, order_id):
        order = get_or_404(Order, Order.id == order_id)
        return order_schema.dump(order).data
