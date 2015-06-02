from flask import jsonify, request, current_app

from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import User


@api.route('/users/<int:user_id>/orders', methods=['GET'])
@require_auth()
def get_user_orders(authenticated_user, user_id):
	""" Gets a particular users orders.
	"""
	user = get_or_404(User, user_id)
	return jsonify(message="Successfully got users orders.", orders=user.orders)
