import datetime
from flask_restful import Resource
from flask import request

from backend import db
from backend.models import User, Session
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import SigninSchema, SessionSchema
from backend.api.v1.exceptions import APIException


class Signin(Resource):
    def post(self):
        load_data = marshal_or_fail('load', request.get_json(), SigninSchema())
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
        return marshal_or_fail('dump', session, SessionSchema())
