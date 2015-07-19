import copy
from flask import jsonify, request, current_app

from backend import db
from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.api.utils import merge_entity_dict_into_entity
from backend.models import Product


# TODO: Adminify.
# TODO: Auth.
@api.route('/products', methods=['PATCH'])
def patch_products():

	patchable_attrs = [
		'name',
		'price_rands',
		'cost_rands',
	]

	products_dict = request.get_json()

	patched_products = []

	for product_dict in products_dict:
		product = get_or_404(Product, product_dict['id'])
		updated_product = merge_entity_dict_into_entity(
			patchable_attrs, 
			product_dict, 
			product,
		)
		patched_products.append(updated_product)
		db.session.add(updated_product)
	db.session.commit()

	return jsonify(
		message="Successfully patched products.", 
		patched_products=patched_products, 
	), 202
