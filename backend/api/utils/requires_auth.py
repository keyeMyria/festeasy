import datetime
from flask import request
from functools import wraps

from backend.models import Session


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        now = datetime.datetime.now()
        auth_token = request.args.get('auth_token')
        if not auth_token:
            raise Exception('No auth token present')
        session = (Session.query.filter(
            Session.token == auth_token,
            )).first()
        if not session:
            raise Exception('No session found with supplied auth_token')
        if session.expires_on < now:
            raise Exception('Session has expired.')
        authenticated_user = session.user
        if not authenticated_user:
            raise Exception('Session has no user.')
        return f(*args, authenticated_user=authenticated_user, **kwargs)
    return decorated
