from flask import jsonify, request, current_app

from backend.api import api
from backend.models import User, Event


@api.route('/events', methods=['GET'])
def get_events():
	""" Gets events.
	"""
	events = Event.query.all()
	return jsonify(message="Successfully got events.", events=events)
