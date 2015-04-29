import datetime
from flask import request, make_response, jsonify
from functools import wraps
from werkzeug.exceptions import Unauthorized

from backend.models import Session


class MyUnauthorized(Unauthorized):
    def __init__(self, msg, status_code=401):
        Unauthorized.__init__(self, msg, response=make_response(
            jsonify(
                success=False,
                message=msg,
            ), status_code, {'WWW-Authenticate': 'xBasic realm="api"'}
        ))  

def require_auth():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            now = datetime.datetime.now()
            authorization_headers = get_authorization_headers_or_401(request)
            authorization_type, encoded_details = authorization_headers
            username, password = decode_details_or_401(encoded_details)
            session = get_valid_session_or_401(password, now)
            request.authenticated_user = session.user
            return f(authenticated_user=request.authenticated_user, *args, **kwargs)
        return decorated_function
    return decorator

def get_authorization_headers_or_401(request):
    authorization_headers = request.headers.get('Authorization')
    if authorization_headers is None:
        raise MyUnauthorized("Received no authentication headers. xBasic "
            "authentication required with username 'api' and a valid session "
            "token as password.")
    authorization_type, encoded_details = authorization_headers.split(' ')
    if authorization_type != 'xBasic':
        raise MyUnauthorized("Authorization type was not xBasic. xBasic "
            "authentication required with a username 'api' and a valid session "
            "token as password.")
    return authorization_type, encoded_details

def decode_details_or_401(encoded_details):
    decoded_details = encoded_details.decode('base64')
    if ':' not in decoded_details:
        raise MyUnauthorized("Encoded details must be ':' seperated. xBasic "
            "authentication required with a username 'api' and a valid session "
            "token as password.")
    username, password = decoded_details.split(':')
    if username != 'api':
        raise MyUnauthorized("Username was not 'api'. xBasic authentication "
            "required with a username 'api' and a valid session token as "
            "password.")
    return username, password

def get_valid_session_or_401(token, now):
    session = Session.query.filter(Session.token==token).first()
    if session is None:
        raise MyUnauthorized("Invalid session token.")
    if session.expires_on < now:
        raise MyUnauthorized("Session expired on %s. Please create a new "
            "session token by signing in." % session.expires_on)
    return session
