from flask_restful import Resource

from backend.models import Order
from backend.api.utils import get_or_404
from backend.api.v1.schemas import ProductSchema


class OrderSingleton(Resource):
    def __init__(self):
        self.order_schema = ProductSchema()

    def get(self, order_id):
        order = get_or_404(Order, Order.id == order_id)
        data, errors = self.order_schema.dump(order)
        return data
