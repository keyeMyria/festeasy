import json
from flask import url_for

from backend import db
from backend.models import User, Product
from backend.testing import APITestCase


class TestCreateProduct(APITestCase):
    def test_create_product_creates_a_product(self):
        """Test that v1.create_product creates a Product.
        """
        user = self.create_user(normal_user=True, 
            is_admin=True, 
            valid_session=True,
            with_cart=True,
        )
        db.session.add(user)
        db.session.commit()


        new_product_name = 'A New Product Name'
        new_product_price_rands = 80
        new_product_cost_rands = 8

        data = dict(
            name=new_product_name,
            cost_rands=new_product_cost_rands,
            price_rands=new_product_price_rands,
        )

        response = self.api_request('post',
            url_for('v1.create_product', user_id=user.id),
            data=data,
            as_user=user,
            with_session=user.sessions[0],
        )

        fetched_product = Product.query.one()
        self.assertEqual(fetched_product.name, new_product_name)
        self.assertEqual(response.json['product']['id'], 1)
        self.assertEqual(response.json['product']['name'], new_product_name)
        self.assertEqual(response.status_code, 200)
