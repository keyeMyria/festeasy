from flask_restful import Resource

from backend.models import OrderProduct
from backend.api.utils import get_or_404
from backend.api.v1.schemas import OrderProductSchema
from backend.api.v1.authentication import requires_auth


order_product_schema = OrderProductSchema()


class OrderProductSingleton(Resource):
    method_decorators = [requires_auth]

    def get(self, order_product_id, authenticated_user):
        order_product = get_or_404(
            OrderProduct,
            OrderProduct.id == order_product_id,
        )
        return order_product_schema.dump(order_product).data
