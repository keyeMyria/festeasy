import datetime
import jwt
from flask import request, jsonify
from functools import wraps
from jwt import DecodeError, ExpiredSignature

from backend.models import User


def parse_token(req):
    token = req.headers.get('Authorization').split()[1]
    return jwt.decode(token, 'secret')


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.headers.get('Authorization'):
            response = jsonify(message='Missing authorization header')
            response.status_code = 401
            return response
        try:
            payload = parse_token(request)
        except DecodeError:
            response = jsonify(message='Token is invalid')
            response.status_code = 401
            return response
        except ExpiredSignature:
            response = jsonify(message='Token has expired')
            response.status_code = 401
        user_id = payload['sub']
        user = User.query.filter(User.id == user_id).first()
        if not user:
            raise Exception('No user for given token. This should never happen.')
        return f(*args, authenticated_user=user, **kwargs)
    return decorated
