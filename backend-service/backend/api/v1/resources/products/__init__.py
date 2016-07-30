from backend.api.v1 import v1_api
from .product_singleton import ProductSingleton
from .product_collection import ProductCollection


v1_api.add_resource(ProductCollection,
                    '/products')
v1_api.add_resource(ProductSingleton,
                    '/products/<int:product_id>')
