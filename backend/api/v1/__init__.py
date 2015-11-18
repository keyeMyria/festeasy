from flask import Blueprint
from flask_restful import Api


v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)

from .resources import auth
from .resources import cart_products
from .resources import carts
from .resources import festivals
from .resources import invoice_products
from .resources import invoices
from .resources import order_products
from .resources import orders
from .resources import payments
from .resources import products
from .resources import sessions
from .resources import users

@v1_bp.route('/')
def hi():
    return 'V1 API Here.'
