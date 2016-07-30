from backend.api.v1 import v1_api
from .cart_product_singleton import CartProductSingleton
from .cart_product_collection import CartProductCollection


v1_api.add_resource(CartProductSingleton,
                    '/cart-products/<int:cart_product_id>')
v1_api.add_resource(CartProductCollection,
                    '/cart-products')
