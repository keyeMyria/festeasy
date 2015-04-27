from flask import jsonify, request, current_app

from backend import db
from backend.api import api
from backend.api.v1.forms import CreateUserForm
from backend.models import User


@api.route('/users', methods=['POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    email_address = create_user_form.email_address.data
    password = create_user_form.password.data
    if not create_user_form.validate():
        return jsonify(error='Invalid email address and or password.'), 401
    user = User(email_address=email_address)
    db.session.add(user)
    db.session.commit()
    return jsonify(user=user.dump()), 201
