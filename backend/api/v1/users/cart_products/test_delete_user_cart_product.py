import json
from flask import url_for

from backend import db
from backend.models import User, UserCartProduct, Product
from backend.utils import APITestCase


class TestDeleteCartUserProduct(APITestCase):
    def test_delete_user_cart_product_delete_user_cart_product(self):
        """ Test that v1.delete_user_cart_products deletes a user_product_cart in the db.
        """
        user = self.create_user(create_valid_session=True)
        product = self.create_product(name='abc', price_cents=99)
        user_cart_product = UserCartProduct()
        user_cart_product.user = user
        user_cart_product.product = product
        db.session.add(user_cart_product)
        db.session.commit()

        response = self.api_request(
            'delete',
            url_for('v1.delete_user_cart_products', user_id=user.id, user_cart_product_ids='1'), 
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['cart_products']), 0)

        self.assertEqual(UserCartProduct.query.all(), list())

    def test_delete_user_cart_product_404s_with_invalid_user_cart_product_id(self):
        """ Test that v1.delete_user_cart_products 404s with an 
        invalid user_cart_product ID.
        """
        user = self.create_user(create_valid_session=True)
        product = self.create_product(name='abc', price_cents=99)
        user_cart_product = UserCartProduct()
        user_cart_product.user = user
        user_cart_product.product = product
        db.session.add(user_cart_product)
        db.session.commit()

        invalid_user_cart_product_id = user_cart_product.id + 1

        response = self.api_request(
            'delete',
            url_for('v1.delete_user_cart_products', user_id=user.id, user_cart_product_ids=invalid_user_cart_product_id), 
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(UserCartProduct.query.one(), user_cart_product)
