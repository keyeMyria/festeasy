from backend.api.v1 import v1_api
from .order_product_collection import OrderProductCollection
from .order_product_singleton import OrderProductSingleton


v1_api.add_resource(OrderProductCollection,
                    '/order-produts')
v1_api.add_resource(OrderProductSingleton,
                    '/order-products/<int:order_product_id>')
