from flask import jsonify

from backend.api import api
from backend.api.v1.forms import CreateUserForm
from backend.models import User


@api.route('/users', methods=['POST'])
def create_user():
	create_user_form = CreateUserForm(request.form)
	if not create_user_form.validate():
		return jsonify(error='Invalid email address and or password.'), 401
	user = User()
	db.sessio.add(user)
	db.sessio.commit()
	return jsonify(user=user), 200
