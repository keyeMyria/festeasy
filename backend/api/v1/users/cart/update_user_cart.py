import logging
from flask import jsonify, request, current_app

from backend import db
from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import User, CartProduct, Event


logger = logging.getLogger(__name__)

@api.route('/users/<int:user_id>/cart', methods=['PATCH'])
@require_auth()
def update_user_cart(authenticated_user, user_id):
	""" Updates a users cart.
	"""

	user = get_or_404(User, user_id)
	cart = user.cart

	if request.get_json()['cart_products']:
		for cp in request.get_json()['cart_products']:
			cart_product_id = cp['id']
			cart_product = get_or_404(CartProduct, cart_product_id)
			cart_product.quantity = cp['quantity']
	else:
		logger.warn("No cart_products to update.")

	if request.get_json()['event']:
		event_id = request.get_json()['event']['id']
		event = get_or_404(Event, event_id)
		cart.event = event
	else:
		logger.warn("No event to update.")

	db.session.add(cart)
	db.session.commit()

	return jsonify(message="Successfully updated cart.", cart=cart), 201
