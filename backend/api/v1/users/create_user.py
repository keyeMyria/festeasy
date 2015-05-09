import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.utils import random_string
from backend.api.v1.forms import CreateUserForm
from backend.models import User, Session


logger = logging.getLogger(__name__)

@api.route('/users', methods=['POST'])
def create_user():
    create_user_form = CreateUserForm(**request.get_json())
    if not create_user_form.validate():
        logger.warn("Failed to create user, form did not validate.")
        return jsonify(message="Failed to create user, form did not validate."), 401

    now = datetime.datetime.now()
    email_address = create_user_form.email_address.data
    password = create_user_form.password.data
    first_name = create_user_form.first_name.data

    existing_user = User.query.filter(User.email_address==email_address).first()
    if existing_user:
        logger.warn("Failed to create user. Email address in use.")
        return jsonify(error_message="Failed to create user. Email address in use."), 409
    
    user = User(
        email_address=email_address, 
        password=password, 
        first_name=first_name
    )
    
    expires_on = now + datetime.timedelta(days=7)
    token = random_string(25)
    session = Session(
        user=user,
        expires_on=expires_on,
        token=token,
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(message='Successfully created user.', user=user.dump(), session=session.dump()), 201
