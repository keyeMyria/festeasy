from flask_restful import Resource

from backend.models import OrderProduct
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import OrderProductSchema


class OrderProductSingleton(Resource):
    def get(self, order_product_id):
        order_product = get_or_404(
            OrderProduct,
            OrderProduct.id == order_product_id,
        )
        return marshal_or_fail('dump', order_product, OrderProductSchema())
