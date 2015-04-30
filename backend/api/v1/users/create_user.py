import json
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.v1.utils import takes_form
from backend.api.v1.forms import CreateUserForm
from backend.models import User


@api.route('/users', methods=['POST'])
@takes_form('CreateUserForm', form_name='create_user_form')
def create_user(create_user_form):
    if not create_user_form.validate():
        return jsonify(message='Invalid email address and or password.'), 401

    email_address = create_user_form.email_address.data
    password = create_user_form.password.data
    first_name = create_user_form.first_name.data

    existing_user = User.query.filter(User.email_address==email_address).first()
    if existing_user:
        return jsonify(error_message='User account already registered with that email address.'), 409
    
    user = User(email_address=email_address, password=password, first_name=first_name)
    db.session.add(user)
    db.session.commit()
    return jsonify(message='successfully created user.', user=user.dump()), 201
