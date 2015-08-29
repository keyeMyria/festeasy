from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import Cart


class TestCartResource(APITestCase):
	def test_get(self):
		cart = Cart()
		db.session.add(cart)
		db.session.commit()
		response = self.api_request(
			'get',
			url_for('v1.cartresource', cart_id=cart.id),
		)
		self.assertEqual(response.json['id'], cart.id)
		self.assertEqual(response.status_code, 200)
