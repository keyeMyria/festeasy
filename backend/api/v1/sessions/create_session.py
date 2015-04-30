import datetime
from flask import jsonify, request

from backend import db
from backend.api import api
from backend.api.v1.utils import takes_form
from backend.api.v1.forms import CreateSessionForm
from backend.models import Session, User
from backend.utils import random_string


@api.route('/sessions', methods=['POST'])
@takes_form('CreateSessionForm', 'create_session_form')
def create_session(create_session_form):
    
    if not create_session_form.validate():
        return jsonify(message='failed to create session. Form did not validate.'), 401

    email_address = create_session_form.email_address.data
    password = create_session_form.password.data

    user = User.query.filter(User.email_address==email_address).first()

    # TODO: email user with password reset on consecutive incorrect login attempts.
    if not user or not user.has_password(password):
    	return jsonify(message='failed to create session. Invalid email address and or password.'), 401

    token = random_string(25)
    expires_on = datetime.datetime.now() + datetime.timedelta(days=7)

    session = Session(
        token=token, 
        user=user, 
        expires_on=expires_on
    )

    db.session.add(session)
    db.session.commit()
    return jsonify(message='successfully created session.', 
    	user=user.dump(), session=session.dump()), 201
