from flask_restful import Resource

from backend.models import Session
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import SessionSchema


class SessionSingleton(Resource):
    def get(self, session_id):
        session = get_or_404(Session, Session.id == session_id)
        return marshal_or_fail('dump', session, SessionSchema())
