from flask_restful import Resource

from backend.models import Session
from backend.api.utils import get_or_404
from backend.api.v1.schemas import SessionSchema


class SessionSingleton(Resource):
    def __init__(self):
        self.session_schema = SessionSchema()

    def get(self, session_id):
        session = get_or_404(Session, Session.id == session_id)
        data, errors = self.session_schema.dump(session)
        return data
