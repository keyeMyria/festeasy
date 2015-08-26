import json
from flask import url_for

from backend import db
from backend.models import User, CartProduct, Product
from backend.models import Cart
from backend.testing import APITestCase


class TestCreateCartUserProducts(APITestCase):
    def test_create_user_cart_product_creates_user_cart_product(self):
        """ Test that v1.create_user_cart_product creates a user_product_cart in the db.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True, create_valid_cart=True)
        user.cart = Cart()
        product = self.create_product(create_valid_product=True)
        db.session.add(user)
        db.session.add(product)
        db.session.commit()

        response = self.api_request(
            'post',
            url_for('v1.create_user_cart_product', user_id=user.id), 
            data=dict(product_id=product.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['cart']['products']), 1)

        user_cart_products = User.query.one().cart.products
        self.assertEqual(len(user_cart_products), 1)
        self.assertEqual(user_cart_products[0], product)

    def test_create_user_cart_products_creates_user_cart_products(self):
        """ Test that v1.create_user_cart_products creates a user_product_cart in the db.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True, create_valid_cart=True)
        user.cart = Cart()
        product = self.create_product(create_valid_product=True)
        db.session.add(user)
        db.session.add(product)
        db.session.commit()

        product_ids = [dict(product_id=product.id)]
        
        response = self.api_request(
            'post',
            url_for('v1.create_user_cart_products', user_id=user.id), 
            data=dict(product_ids=product_ids),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json['cart']['products']), 1)

        user_cart_products = User.query.one().cart.products
        self.assertEqual(len(user_cart_products), 1)
        self.assertEqual(user_cart_products[0], product)

    def test_create_user_cart_product_400s_with_bad_form(self):
        """ Test that v1.create_user_cart_products 400s when
        the form is not valid.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True, create_valid_cart=True)
        product = self.create_product(create_valid_product=True)
        db.session.add(user)
        db.session.add(product)
        db.session.commit()

        product_ids = [dict(an_invalid_key=product.id)]
        
        response = self.api_request(
            'post',
            url_for('v1.create_user_cart_products', user_id=user.id), 
            data=dict(product_ids=product_ids),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 400)

    def test_create_user_cart_products_409s(self):
        """ Test that v1.create_user_cart_products 409s with dup.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True, create_valid_cart=True)
        user.cart = Cart()
        product = self.create_product(create_valid_product=True)
        user.cart.products.append(product)
        db.session.add(user)
        db.session.add(product)
        db.session.commit()

        product_ids = [dict(product_id=product.id)]
        
        response = self.api_request(
            'post',
            url_for('v1.create_user_cart_products', user_id=user.id), 
            data=dict(product_ids=product_ids),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 409)

    def test_create_user_cart_product_409s(self):
        """ Test that v1.create_user_cart_product 409s with dup.
        """
        user = self.create_user(create_normal_user=True, create_valid_session=True)
        user.cart = Cart()
        product = self.create_product(create_valid_product=True)
        user.cart.products.append(product)
        db.session.add(user)
        db.session.add(product)
        db.session.commit()
        
        response = self.api_request(
            'post',
            url_for('v1.create_user_cart_product', user_id=user.id), 
            data=dict(product_id=product.id),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 409)
