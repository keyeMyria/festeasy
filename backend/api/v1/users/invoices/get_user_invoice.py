from flask import jsonify, request, current_app

from backend.api import api
from backend.api.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import User, Invoice


@api.route('/users/<int:user_id>/invoice/<int:invoice_id>', methods=['GET'])
@require_auth()
def get_user_invoice(authenticated_user, user_id, invoice_id):
	""" Gets a particular user.
	"""
	user = get_or_404(User, user_id)
	invoice = get_or_404(Invoice, invoice_id)
	return jsonify(message="Successfully got user invoice.", invoice=invoice)
