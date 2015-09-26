from backend.api.v1 import v1_api
from .carts_singleton import CartSingleton


v1_api.add_resource(CartSingleton,
                    '/carts/<int:cart_id>')
