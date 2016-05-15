from flask import Blueprint, jsonify
from flask_restful import Api

from backend.exceptions import APIException

v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)

from .resources import auth
from .resources import cart_products
from .resources import carts
from .resources import collections
from .resources import festivals
from .resources import invoice_products
from .resources import invoices
from .resources import order_products
from .resources import orders
from .resources import packaged_stock_units
from .resources import packages
from .resources import payments
from .resources import products
from .resources import sessions
from .resources import users
from .resources import categories
from .resources import suppliers
from .resources import stock_units
from .resources import forgot_password_tokens
from .resources import payu


@v1_bp.errorhandler(APIException)
def handle_api_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@v1_bp.route('/')
def hi():
    return 'V1 API Here.'
