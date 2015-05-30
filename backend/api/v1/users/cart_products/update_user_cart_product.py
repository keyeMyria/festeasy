from flask import jsonify, request, current_app

from backend import db
from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import User, UserCartProduct


@api.route('/users/<int:user_id>/cart_products/<int:user_cart_product_id>', methods=['PATCH'])
@require_auth()
def update_user_cart_product(authenticated_user, user_id, user_cart_product_id):
	""" Updates a particular user_cart_product.
	"""
	can_patch = [
		'quantity',
		]
	user = get_or_404(User, user_id)
	user_cart_product = get_or_404(UserCartProduct, user_cart_product_id)

	user_cart_product.quantity = request.get_json()['quantity']

	db.session.add(user_cart_product)
	db.session.commit()

	return jsonify(message="Successfully updated user_cart_product.", user_cart_products=user.user_cart_products), 201
