from flask_restful import Resource

from backend.models import Order
from backend.api.v1.schemas import OrderSchema


order_schema = OrderSchema()


class UserOrderCollection(Resource):
    def get(self, user_id):
        orders = Order.query.filter(Order.user_id == user_id).all()
        return order_schema.dump(orders, many=True).data
