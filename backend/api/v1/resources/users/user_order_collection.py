from flask_restful import Resource

from backend.models import Order
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import OrderSchema


class UserOrderCollection(Resource):
    def get(self, user_id):
        orders = Order.query.filter(Order.user_id == user_id).all()
        return marshal_or_fail('dump', orders, OrderSchema(), many=True)
