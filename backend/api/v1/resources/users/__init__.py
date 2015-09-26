from backend.api.v1 import v1_api
from .users_singleton import UserSingleton
from .users_collection import UserCollection
from .user_carts_singleton import UserCartSingleton
from .user_orders_singleton import UserOrderSingleton
from .user_orders_collection import UserOrderCollection


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
