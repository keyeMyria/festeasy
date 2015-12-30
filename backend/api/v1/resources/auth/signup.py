import datetime
from flask_restful import Resource
from flask import request

from backend import db
from backend.tasks import send_templated_email
from backend.models import User, Session, Cart
from backend.api.v1.schemas import SignupSchema, SessionSchema
from backend.exceptions import APIException


signup_schema = SignupSchema()
session_schema = SessionSchema()


class Signup(Resource):
    def post(self):
        load_data = signup_schema.load(request.get_json()).data
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
        send_templated_email(
            user.email_address,
            'Welcome',
            'signup.html',
            dict(
                first_name=user.first_name,
            ),
        )
        return session_schema.dump(session).data
