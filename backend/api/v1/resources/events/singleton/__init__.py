from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import Event
from backend.api.utils import get_or_404


singleton_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('name')


class EventSingleton(Resource):
    @marshal_with(singleton_fields)
    def get(self, event_id):
        event = get_or_404(Event, Event.id == event_id)
        return event

    @marshal_with(singleton_fields)
    def delete(self, event_id):
        event = get_or_404(Event, Event.id == event_id)
        db.session.delete(event)
        db.session.commit()
        return event

    @marshal_with(singleton_fields)
    def patch(self, event_id):
        args = patch_parser.parse_args(strict=True)
        event = get_or_404(Event, Event.id == event_id)
        for arg in args:
            setattr(event, arg, args[arg])
        db.session.add(event)
        db.session.commit()
        return event
