import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.utils import get_or_404
from backend.api.auth import require_auth
from backend.api.forms import SetCurrentCartEventForm
from backend.models import User, Event


logger = logging.getLogger(__name__)

@api.route('/users/<int:user_id>/current_cart_event', methods=['POST'])
@require_auth()
def set_current_cart_event(authenticated_user, user_id):
    """ Sets a users current_cart_event.
    """
    set_current_cart_event_form = SetCurrentCartEventForm(**request.get_json())
    if not set_current_cart_event_form.validate():
        logger.warn("Failed to set current_cart_event for user, form did not validate.")
        return jsonify(message="Failed to set current_cart_event for user, form did not validate."), 400

    user = get_or_404(User, user_id)

    event_id = set_current_cart_event_form.event_id.data
    event = get_or_404(Event, event_id)

    user.current_cart_event = event
    db.session.add(user)
    db.session.commit()

    return jsonify(message="Successfully set user current_cart_event.", user=user), 201
