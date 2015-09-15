import datetime
import jwt
from flask_restful import Resource
from flask import request, jsonify, make_response

from backend import db
from backend.models import User, Session
from backend.api.v1.schemas import SigninSchema, UserSchema, SessionSchema
from backend.api.v1.exceptions import APIException


class Signin(Resource):
    def __init__(self):
        self.signin_schema = SigninSchema()
        self.user_schema = UserSchema()
        self.session_schema = SessionSchema()

    def post(self):
        load_data, load_erros = self.signin_schema.load(request.get_json())
        email_address = load_data['email_address']
        password = load_data['password']
        user = User.query.filter(
            User.email_address == email_address,
            ).first()
        if not user or not user.has_password(password):
            raise APIException(
                'Incorrect email address and password combination.',
                401,
            )
        now = datetime.datetime.utcnow()
        expires_on = now + datetime.timedelta(days=14)
        session = Session(
            expires_on=expires_on,
            user=user,
        )
        session.generate_token()
        db.session.add(session)
        db.session.commit()
        session_data, session_errors = self.session_schema.dump(session)
        return make_response(jsonify(session_data), 201)
