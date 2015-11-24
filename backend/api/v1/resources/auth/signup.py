import datetime
from flask_restful import Resource
from flask import request

from backend import db
from backend.models import User, Session, Cart
from backend.api.utils import marshal_or_fail
from backend.api.v1.schemas import SignupSchema, SessionSchema
from backend.api.v1.exceptions import APIException


class Signup(Resource):
    def post(self):
        load_data = marshal_or_fail('load', request.get_json(), SignupSchema())
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
        return marshal_or_fail('dump', session, SessionSchema())
