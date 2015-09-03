from flask_restful import Resource

from backend.models import Order
from backend.api.v1.schemas import OrderSchema


class UserOrderCollection(Resource):
    def __init__(self):
        self.order_schema = OrderSchema()

    def get(self, user_id):
        orders = Order.query.filter(Order.user_id == user_id).all()
        data, errors = self.order_schema.dump(orders, many=True)
        return data
