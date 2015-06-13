from flask import jsonify, request, current_app

from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import Product


@api.route('/products', methods=['GET'])
def get_products():
	products = Product.query.all()
	return jsonify(message="Successfully got products.", products=products), 200
