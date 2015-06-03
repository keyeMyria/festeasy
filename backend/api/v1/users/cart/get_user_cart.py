from flask import jsonify, request, current_app

from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import User


@api.route('/users/<int:user_id>/cart', methods=['GET'])
@require_auth()
def get_user_cart(authenticated_user, user_id):
	""" Gets a particular users cart.
	"""
	user = get_or_404(User, user_id)
	return jsonify(message="Successfully got users cart.", cart=user.cart)
