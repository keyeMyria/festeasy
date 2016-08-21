from flask_restful import Resource

from backend.models import Order
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderSchema
from backend.api.v1.authentication import requires_auth


order_schema = OrderSchema()


class OrderSingleton(Resource):
    method_decorators = [requires_auth]

    def get(self, order_id, authenticated_user):
        order = get_or_404(Order, Order.id == order_id)
        return order_schema.dump(order).data
