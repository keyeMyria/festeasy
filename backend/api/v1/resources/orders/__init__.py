from backend.api.v1 import v1_api
from .order_singleton import OrderSingleton


v1_api.add_resource(OrderSingleton,
                    '/orders/<int:order_id>')
