import datetime
from flask_restful import Resource
from flask import request, jsonify

from backend import db
from backend.models import User, Session, Cart
from backend.api.v1.schemas import SignupSchema, UserSchema, SessionSchema
from backend.utils import random_string


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
            raise Exception('User with email address supplied already exists.')
        user = User(**load_data)
        user.cart = Cart()
        now = datetime.datetime.now()
        token = random_string(25)
        session = Session(
            expires_on=now + datetime.timedelta(days=100),
            token=token,
        )
        user.sessions.append(session)
        db.session.add(user)
        db.session.commit()
        user_data, user_errors = self.user_schema.dump(user)
        session_data, session_errors = self.session_schema.dump(session)
        return jsonify(user=user_data, session=session_data)
