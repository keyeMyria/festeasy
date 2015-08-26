import json
from flask import url_for

from backend import db
from backend.models import User, Product
from backend.testing import APITestCase


class TestPatchProducts(APITestCase):
    def test_patch_products_patches_products(self):
        """ Test that v1.patch_products patches products.
        """
        user = self.create_user(
            first_name='A name',
            email_address="asd@asd.com",
            password='123',
            is_admin=True,
            create_valid_session=True,
            create_valid_cart=True,
        )
        product = self.create_product(
            name='Test Product',
            price_rands=123,
            cost_rands=111,
        )
        db.session.add(user)
        db.session.add(product)
        db.session.commit()

        new_product_name = 'A New Product Name'
        data = [
            dict(
                id=product.id,
                name=new_product_name,
            ),
        ]

        response = self.api_request('patch',
            url_for('v1.patch_products', user_id=user.id),
            data=data,
            as_user=user,
            with_session=user.sessions[0],
        )

        fetched_product = Product.query.one()
        self.assertEqual(fetched_product.name, new_product_name)
        self.assertEqual(response.json['patched_products'][0]['id'], product.id)
        self.assertEqual(response.json['patched_products'][0]['name'], new_product_name)
        self.assertEqual(response.status_code, 202)
