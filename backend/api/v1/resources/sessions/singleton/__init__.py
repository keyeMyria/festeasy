from flask_restful import Resource, fields, marshal_with

from backend.models import Session
from backend.api.utils import get_or_404


singleton_fields = {
    'id': fields.Integer,
}


class SessionSingleton(Resource):
    @marshal_with(singleton_fields)
    def get(self, session_id):
        session = get_or_404(Session, Session.id == session_id)
        return session
