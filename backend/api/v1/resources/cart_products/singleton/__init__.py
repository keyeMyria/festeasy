from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.api.utils import get_or_404
from backend.models import CartProduct


singleton_fields = {
	'id': fields.Integer,
	'product_id': fields.Integer,
	'cart_id': fields.Integer,
	'quantity': fields.Integer,
	'sub_total_rands': fields.Float,
}

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('quantity', type=int)

class CartProductSingleton(Resource):
	@marshal_with(singleton_fields)
	def get(self, cart_product_id):
		cart_product = get_or_404(CartProduct, CartProduct.id == cart_product_id)
		return cart_product

	@marshal_with(singleton_fields)
	def patch(self, cart_product_id):
		args = patch_parser.parse_args(strict=True)
		cart_product = get_or_404(CartProduct, CartProduct.id == cart_product_id)
		for arg in args:
			setattr(cart_product, arg, args[arg])
		db.session.add(cart_product)
		db.session.commit()
		return cart_product
