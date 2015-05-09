import json
from flask import url_for

from backend import db
from backend.models import User, UserCartProduct, Product
from backend.utils import APITestCase


class TestCreateCartUserProduct(APITestCase):
    def test_create_user_cart_product_creates_user_cart_product(self):
        """ Test that v1.create_user_cart_product creates a user_product_cart in the db.
        """
        user = self.create_user(create_valid_session=True)
        product = self.create_product(name='abc', price_cents=99)
        db.session.add(user)
        db.session.add(product)
        db.session.commit()

        product_ids = list()
        product_ids.append(dict(product_id=product.id))
        
        response = self.api_request(
            'post',
            url_for('v1.create_user_cart_product', user_id=user.id), 
            data=dict(product_ids=product_ids),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        products = User.query.one().cart_products
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0], product)

        self.assertEqual(Product.query.one().cart_users[0], user)
        self.assertIsNotNone(response.json['cart_products'])
