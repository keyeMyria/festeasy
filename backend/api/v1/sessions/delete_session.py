import datetime
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.v1.auth import require_auth
from backend.api.utils import get_or_404
from backend.models import Session


@api.route('/sessions/<int:session_id>', methods=['DELETE'])
@require_auth()
def delete_session(authenticated_user, session_id):
	session = get_or_404(Session, session_id)
	db.session.delete(session)
	db.session.commit()
	return jsonify(session=session.dump(), message="Successfully deleted session."), 201
