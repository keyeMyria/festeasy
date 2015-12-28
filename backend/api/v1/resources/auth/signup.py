import datetime
from flask_restful import Resource
from flask import request
from jinja2 import Environment, PackageLoader

from backend import db, emailer
from backend.models import User, Session, Cart
from backend.api.v1.schemas import SignupSchema, SessionSchema
from backend.api.v1.exceptions import APIException


signup_schema = SignupSchema()
session_schema = SessionSchema()

env = Environment(loader=PackageLoader('backend', 'email_templates'))
template = env.get_template('signup.tmpl.html')


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
        emailer.send_email(
            user.email_address,
            'FestEasy',
            'info@festeasy.co.za',
            'Welcome',
            template.render(
                first_name=user.first_name,
            )
        )
        return session_schema.dump(session).data
