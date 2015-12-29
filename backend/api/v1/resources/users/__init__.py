from backend.api.v1 import v1_api
from .user_singleton import UserSingleton
from .user_collection import UserCollection
from .user_cart_singleton import UserCartSingleton
from .user_order_singleton import UserOrderSingleton
from .user_order_collection import UserOrderCollection
from .user_cart_cart_product_collection import UserCartCartProductCollection
from .change_password import ChangePassword


v1_api.add_resource(UserCollection,
                    '/users')
v1_api.add_resource(UserSingleton,
                    '/users/<int:user_id>')
v1_api.add_resource(UserCartSingleton,
                    '/users/<int:user_id>/cart')
v1_api.add_resource(UserOrderCollection,
                    '/users/<user_id>/orders')
v1_api.add_resource(UserOrderSingleton,
                    '/users/<int:user_id>/orders/<order_id>')
v1_api.add_resource(UserCartCartProductCollection,
                    '/users/<int:user_id>/cart/cart-products')
v1_api.add_resource(ChangePassword,
                    '/users/<int:user_id>/change-password')
