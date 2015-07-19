from flask import jsonify, request, current_app

from backend import db
from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.api.utils import merge_entity_dict_into_entity
from backend.models import Product

# TODO: Auth.
# TODO: Adminify.
@api.route('/products', methods=['POST'])
def create_product():

	allowed_attrs = [
		'name',
		'is_enabled',
		'cost_rands',
		'price_rands',
	]

	product_dict = request.get_json()
	product = Product()

	product = merge_entity_dict_into_entity(allowed_attrs, product_dict, product)
	db.session.add(product)
	db.session.commit()

	return jsonify(message="Successfully created product.", product=product), 200
