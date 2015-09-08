from flask import Blueprint
from flask_restful import Api


v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)


@v1_bp.route('/')
def hi():
    return 'V1 API Here.'

from .resources.auth import Signup
v1_api.add_resource(Signup,
                    '/signup')

from .resources.auth import Signin
v1_api.add_resource(Signin,
                    '/signin')

from .resources.users import UserCollection
v1_api.add_resource(UserCollection,
                    '/users')
from .resources.users import UserSingleton
v1_api.add_resource(UserSingleton,
                    '/users/<int:user_id>')
from .resources.users import UserCartSingleton
v1_api.add_resource(UserCartSingleton,
                    '/users/<int:user_id>/cart')
from .resources.users import UserOrderCollection
v1_api.add_resource(UserOrderCollection,
                    '/users/<user_id>/orders')
from .resources.users import UserOrderSingleton
v1_api.add_resource(UserOrderSingleton,
                    '/users/<int:user_id>/orders/<order_id>')

from .resources.carts import CartSingleton
v1_api.add_resource(CartSingleton,
                    '/carts/<int:cart_id>')

from .resources.cart_products import CartProductSingleton
v1_api.add_resource(CartProductSingleton,
                    '/cart-products/<int:cart_product_id>')

from .resources.events import EventSingleton
v1_api.add_resource(EventSingleton,
                    '/events/<int:event_id>')

from .resources.invoices import InvoiceSingleton
v1_api.add_resource(InvoiceSingleton,
                    '/invoices/<int:invoice_id>')

from .resources.invoice_products import InvoiceProductSingleton
v1_api.add_resource(InvoiceProductSingleton,
                    '/invoice-products/<int:invoice_product_id>')

from .resources.orders import OrderSingleton
v1_api.add_resource(OrderSingleton,
                    '/orders/<int:order_id>')

from .resources.order_products import OrderProductSingleton
v1_api.add_resource(OrderProductSingleton,
                    '/order-products/<int:order_product_id>')

from .resources.payments import PaymentSingleton
v1_api.add_resource(PaymentSingleton,
                    '/payments/<int:payment_id>')

from .resources.products import ProductSingleton
v1_api.add_resource(ProductSingleton,
                    '/products/<int:product_id>')

from .resources.sessions import SessionSingleton
v1_api.add_resource(SessionSingleton,
                    '/sessions/<int:session_id>')
