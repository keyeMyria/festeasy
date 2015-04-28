from flask import jsonify, request, current_app

from backend.api import api
from backend.api.utils import get_or_404
from backend.models import User


@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	user = get_or_404(User, user_id)
	return jsonify(user=user.dump())
