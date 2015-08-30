from flask import Blueprint
from flask_restful import Api


v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)

@v1_bp.route('/')
def hi():
	return 'V1 API Here.'

from .resources.users import UserSingleton
v1_api.add_resource(UserSingleton, '/users/<int:user_id>')
from .resources.users import UserCollection
v1_api.add_resource(UserCollection, '/users')

from .resources.carts import CartSingleton
v1_api.add_resource(CartSingleton, '/carts/<int:cart_id>')

from .resources.cart_products import CartProductSingleton
v1_api.add_resource(CartProductSingleton, '/cart-products/<int:cart_product_id>')

from .resources.events import EventSingleton
v1_api.add_resource(EventSingleton, '/events/<int:event_id>')

from .resources.invoices import InvoiceSingleton
v1_api.add_resource(InvoiceSingleton, '/invoices/<int:invoice_id>')
