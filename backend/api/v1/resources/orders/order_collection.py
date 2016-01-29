from flask_restful import Resource

from backend.models import Order
from backend.api.v1.schemas import OrderSchema


order_schema = OrderSchema()


class OrderCollection(Resource):
    def get(self):
        orders = Order.query.all()
        return order_schema.dump(orders, many=True).data
