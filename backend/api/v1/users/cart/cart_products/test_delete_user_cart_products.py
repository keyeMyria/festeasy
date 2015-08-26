import json
from flask import url_for

from backend import db
from backend.models import User, CartProduct, Product
from backend.models import Cart
from backend.testing import APITestCase


class TestDeleteCartUserProducts(APITestCase):
    def test_delete_user_cart_product_delete_user_cart_products(self):
        """ Test that v1.delete_user_cart_products deletes a user_product_cart in the db.
        """
        user = self.create_user(normal_user=True, valid_session=True)
        user.cart = Cart()
        product = self.create_product(create_valid_product=True)
        cart_product = CartProduct(
            cart=user.cart,
            product=product
            )
        db.session.add(cart_product)
        db.session.commit()

        response = self.api_request(
            'delete',
            url_for('v1.delete_user_cart_products', user_id=user.id, cart_product_ids='1'), 
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['cart']['products']), 0)

        self.assertEqual(CartProduct.query.all(), list())

    def test_delete_user_cart_products_404s_with_invalid_user_cart_product_id(self):
        """ Test that v1.delete_user_cart_products 404s with an 
        invalid user_cart_product ID.
        """
        user = self.create_user(normal_user=True, valid_session=True)
        user.cart = Cart()
        product = self.create_product(create_valid_product=True)
        cart_product = CartProduct(
            cart=user.cart,
            product=product
            )
        db.session.add(cart_product)
        db.session.commit()

        invalid_cart_product_id = cart_product.id + 1

        response = self.api_request(
            'delete',
            url_for('v1.delete_user_cart_products', user_id=user.id, cart_product_ids=invalid_cart_product_id), 
            as_user=user,
            with_session=user.sessions[0],
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(CartProduct.query.one(), cart_product)
