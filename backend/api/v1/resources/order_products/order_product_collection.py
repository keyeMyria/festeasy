from flask_restful import Resource

from backend.models import OrderProduct
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import OrderProductSchema


class OrderProductCollection(Resource):
    def get(self):
        q = OrderProduct.query
        order_products = q.all()
        return marshal_or_fail(
            'dump',
            order_products,
            OrderProductSchema(),
            many=True,
        )
