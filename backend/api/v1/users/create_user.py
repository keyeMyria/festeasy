import datetime
import json
import logging
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.utils import random_string
from backend.api.forms import CreateUserForm
from backend.models import User, Session, Cart


logger = logging.getLogger(__name__)

def _create_normal_user(email_address, password, first_name, guest_token):
    now = datetime.datetime.utcnow()
    existing_user = (User.query
        .filter(User.email_address==email_address)
        .first())
    if existing_user:
        logger.warn("Failed to create user. Email address in use.")
        return jsonify(message="Failed to create user. Email address in use."), 409

    if guest_token:
        existing_guest_user = (User.query
            .filter(User.guest_token==guest_token)
            .first())
        if existing_guest_user:
            user = existing_guest_user
        else:
            logger.error("Was given guest_token {guest_token} but no user was found with it."
                .format(guest_token=guest_token))
            raise Exception("Was given guest_token {guest_token} but no user was found with it."
                .format(guest_token=guest_token))
    else:
        user = User(cart=Cart())

    user.email_address = email_address
    user.set_password(password)
    user.first_name = first_name
    
    expires_on = now + datetime.timedelta(days=100)
    token = random_string(25)
    session = Session(
        user=user,
        expires_on=expires_on,
        token=token,
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(message='Successfully created normal user.', user=user, session=session), 201

def _create_guest_user(guest_token):
    now = datetime.datetime.utcnow()
    if not guest_token:
        logger.error("guest_token cannot be '{type}'"
            .format(type=type(guest_token)))
        raise Exception("guest_token cannot be '{type}'"
            .format(type=type(guest_token)))

    existing_guest_user = (User.query
        .filter(User.guest_token==guest_token)
        .first())

    if existing_guest_user:
        logger.warn("User with guest_token '{guest_token}'' already exists."
            .format(guest_token=guest_token))
        return jsonify(message="User with guest_token '{guest_token}'' already exists.".format(guest_token=guest_token)), 409

    user = User(guest_token=guest_token, cart=Cart())

    expires_on = now + datetime.timedelta(days=100)
    token = random_string(25)
    session = Session(
        user=user,
        expires_on=expires_on,
        token=token,
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(message='Successfully created guest user.', user=user, session=session), 201

@api.route('/users', methods=['POST'])
def create_user():
    """ Creates a new user.
    """
    create_user_form = CreateUserForm(**request.get_json())
    if not create_user_form.validate():
        logger.warn("Failed to create user, form did not validate.")
        return jsonify(message="Failed to create user, form did not validate."), 400

    email_address = create_user_form.email_address.data
    password = create_user_form.password.data
    first_name = create_user_form.first_name.data
    guest_token = create_user_form.guest_token.data

    if email_address and password and first_name:
        return _create_normal_user(
            email_address,
            password,
            first_name,
            guest_token,
            )
    elif not any([email_address, password, first_name]) and guest_token:
        return _create_guest_user(guest_token)
    else:
        return jsonify(message="Failed to create user"), 400
