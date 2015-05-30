import json
from flask import url_for

from backend import db
from backend.models import User, UserCartProduct, Product
from backend.utils import APITestCase


class TestUpdateUserCartProducts(APITestCase):
    def test_update_user_cart_product(self):
        """ Test that v1.update_user_cart_product updates quantity.
        """
        user = self.create_user(create_valid_session=True)
        product = self.create_product(name='abc', price_rands=99)
        user.cart_products.append(product)
        db.session.add(user)
        db.session.commit()

        user_cart_product = UserCartProduct.query.one()
        old_quantity = user_cart_product.quantity

        new_quantity = old_quantity + 10

        response = self.api_request(
            'patch',
            url_for('v1.update_user_cart_product', user_id=user.id, user_cart_product_id=user_cart_product.id), 
            data=dict(quantity=new_quantity),
            as_user=user,
            with_session=user.sessions[0],
        )
        
        self.assertEqual(response.status_code, 201)
        fetched_user_cart_product = UserCartProduct.query.one()
        self.assertEqual(fetched_user_cart_product.quantity, new_quantity)
        self.assertIsNotNone(response.json['user_cart_products'])
