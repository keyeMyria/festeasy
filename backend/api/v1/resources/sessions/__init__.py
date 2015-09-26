from backend.api.v1 import v1_api
from .sessions_singleton import SessionSingleton


v1_api.add_resource(SessionSingleton,
                    '/sessions/<int:session_id>')
