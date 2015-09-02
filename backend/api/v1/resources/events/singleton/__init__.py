from flask_restful import Resource
from flask import request

from backend import db
from backend.models import Event
from backend.api.utils import get_or_404
from backend.api.v1.schemas import EventSchema


class EventSingleton(Resource):
    def __init__(self):
        self.event_schema = EventSchema()

    def get(self, event_id):
        event = get_or_404(Event, Event.id == event_id)
        data, errors = self.event_schema.dump(event)
        return data

    def patch(self, event_id):
        event = get_or_404(Event, Event.id == event_id)
        load_data, load_errors = self.event_schema.load(request.get_json())
        for arg in load_data:
            setattr(event, arg, load_data[arg])
        db.session.add(event)
        db.session.commit()
        data, errors = self.event_schema.dump(event)
        return data
