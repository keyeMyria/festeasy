import datetime
from flask_restful import Resource
from flask import request, jsonify, make_response

from backend import db
from backend.models import User, Session, Cart
from backend.api.v1.schemas import SignupSchema, UserSchema, SessionSchema
from backend.api.v1.exceptions import APIException


class Signup(Resource):
    def __init__(self):
        self.signup_schema = SignupSchema()
        self.user_schema = UserSchema()
        self.session_schema = SessionSchema()

    def post(self):
        load_data, load_erros = self.signup_schema.load(request.get_json())
        existing_user = User.query.filter(
            User.email_address == load_data['email_address']
            ).first()
        if existing_user:
            raise APIException(
                'A user with that email address already exists.',
                409,
                )
        user = User(**load_data)
        user.cart = Cart()
        now = datetime.datetime.now()
        session = Session(
            expires_on=now + datetime.timedelta(days=100),
            user=user,
        )
        session.generate_token()
        db.session.add(session)
        db.session.commit()
        session_data, session_errors = self.session_schema.dump(session)
        return make_response(jsonify(session_data), 201)
