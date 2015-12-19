from backend.api.v1 import v1_api
from .product_stock_collection import ProductStockCollection


v1_api.add_resource(ProductStockCollection,
                    '/product-stocks')
