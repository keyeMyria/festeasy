import datetime
from flask_restful import Resource
from flask import request

from backend import db
from backend.models import User, Session
from backend.api.v1.schemas import SigninSchema, SessionSchema
from backend.exceptions import APIException


signin_schema = SigninSchema()
session_schema = SessionSchema()


class Signin(Resource):
    def post(self):
        load_data = signin_schema.load(request.get_json()).data
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
        now = datetime.datetime.now()
        expires_on = now + datetime.timedelta(days=14)
        session = Session(
            expires_on=expires_on,
            user=user,
        )
        session.generate_token()
        db.session.add(session)
        db.session.commit()
        return {'session': session_schema.dump(session).data}
