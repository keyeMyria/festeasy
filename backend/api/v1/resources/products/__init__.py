from backend.api.v1 import v1_api
from .products_singleton import ProductSingleton


v1_api.add_resource(ProductSingleton,
                    '/products/<int:product_id>')
