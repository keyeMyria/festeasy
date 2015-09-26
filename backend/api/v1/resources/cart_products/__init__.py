from backend.api.v1 import v1_api
from .cart_products_singleton import CartProductSingleton


v1_api.add_resource(CartProductSingleton,
                    '/cart-products/<int:cart_product_id>')
