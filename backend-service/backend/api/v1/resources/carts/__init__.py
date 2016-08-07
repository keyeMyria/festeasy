from backend.api.v1 import v1_api
from .cart_singleton import CartSingleton
from .cart_checkout import CartCheckout


v1_api.add_resource(
    CartSingleton,
    '/carts/<int:cart_id>'
)

v1_api.add_resource(
    CartCheckout,
    '/carts/<int:cart_id>/checkout'
)
