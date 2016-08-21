from flask_restful import Resource

from backend.models import Order
from backend.api.v1.schemas import OrderSchema
from backend.api.v1.authentication import requires_auth


order_schema = OrderSchema()


class OrderCollection(Resource):
    method_decorators = [requires_auth]

    def get(self, authenticated_user):
        orders = Order.query.all()
        return order_schema.dump(orders, many=True).data
