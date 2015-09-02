from flask_restful import Resource

from backend.models import OrderProduct
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderProductSchema


class OrderProductSingleton(Resource):
    def __init__(self):
        self.order_product_schema = OrderProductSchema()

    def get(self, order_product_id):
        order_product = get_or_404(
            OrderProduct,
            OrderProduct.id == order_product_id,
        )
        data, errors = self.order_product_schema.dump(order_product)
        return data
