import json
from flask import url_for

from backend import db
from backend.models import User, UserCartProduct, Product
from backend.utils import APITestCase


class TestDeleteCartUserProduct(APITestCase):
    def test_delete_user_cart_product_delete_user_cart_product(self):
        """ Test that v1.delete_user_cart_product deletes a user_product_cart in the db.
        """
        user = self.create_user(create_valid_session=True)
        product = self.create_product(name='abc', price_cents=99)
        user_cart_product = UserCartProduct()
        user_cart_product.user = user
        user_cart_product.product = product
        db.session.add(user_cart_product)
        db.session.commit()

        user_cart_product_ids = list()
        user_cart_product_ids.append(dict(user_cart_product_id=product.id))
        
        response = self.api_request(
            'delete',
            url_for('v1.delete_user_cart_product', user_id=user.id), 
            data=dict(user_cart_product_ids=user_cart_product_ids),
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['cart_products']), 0)

        self.assertEqual(UserCartProduct.query.all(), list())
