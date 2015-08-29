from flask_restful import Resource, fields, marshal_with

from backend import db
from backend.models import User, Cart

resource_fields = {
	'id': fields.Integer,
	'email_address': fields.String,
}

class UserListResource(Resource):
	def get(self):
		user = User()
		user.cart = Cart()
		user.set_password('123')
		user.email_address='asd@awds.com'
		user.first_name = 'Jason'
		db.session.add(user)
		db.session.commit()
		return user.id

class UserResource(Resource):
	@marshal_with(resource_fields)
	def get(self, user_id):
		user = User.query.filter(User.id==user_id).first()
		return user

	@marshal_with(resource_fields)
	def delete(self, user_id):
		user = User.query.filter(User.id==user_id).first()
		db.session.delete(user)
		db.session.commit()
		return user

