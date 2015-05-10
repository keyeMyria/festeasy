from flask import jsonify, request, current_app

from backend.api import api
from backend.api.v1.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import Product


@api.route('/products', methods=['GET'])
def get_products():
	products = Product.query.all()
	dumnped_products = list()
	for product in products:
		dumnped_products.append(product.dump())
	return jsonify(message="Successfully got products.", products=dumnped_products), 200
