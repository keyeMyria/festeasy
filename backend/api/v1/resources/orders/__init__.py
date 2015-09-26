from backend.api.v1 import v1_api
from .orders_singleton import OrderSingleton


v1_api.add_resource(OrderSingleton,
                    '/orders/<int:order_id>')
