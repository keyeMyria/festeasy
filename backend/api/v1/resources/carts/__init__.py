from backend.api.v1 import v1_api
from .cart_singleton import CartSingleton
from .cart_singleton_checkout import CartSingletonCheckout

v1_api.add_resource(CartSingleton,
                    '/carts/<int:cart_id>')

v1_api.add_resource(CartSingletonCheckout,
                    '/carts/<int:cart_id>/checkout')
