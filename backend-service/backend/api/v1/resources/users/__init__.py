from backend.api.v1 import v1_api
from .user_singleton import UserSingleton
from .user_collection import UserCollection
from .change_password import ChangePassword


v1_api.add_resource(UserCollection,
                    '/users')
v1_api.add_resource(UserSingleton,
                    '/users/<int:user_id>')
v1_api.add_resource(ChangePassword,
                    '/users/<int:user_id>/change-password')
