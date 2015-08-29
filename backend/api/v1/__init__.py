from flask import Blueprint
from flask_restful import Api

from .resources import UserResource
from .resources import UserListResource
from .resources import CartResource


v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)

v1_api.add_resource(UserResource, '/users/<int:user_id>')
v1_api.add_resource(CartResource, '/users/<int:user_id>/carts/<int:cart_id>', endpoint='v1.userresource.cartresource')
v1_api.add_resource(UserListResource, '/users')
v1_api.add_resource(CartResource, '/carts/<int:cart_id>')
