from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.usercartcartproductcollection'


class TestUserCartCartProductCollection(APITestCase):
    def test_get(self):
        """
        Test that only a specific user's cart products are returned,
        with a 200 status.
        """
        user = self.create_user(
            normal_user=True,
            with_cart=True,
        )
        cart_product = self.create_cart_product(
            product=self.create_product(create_valid_product=True),
            cart=user.cart,
        )
        other_user = self.create_user(
            normal_user=True,
            with_cart=True,
            email_address='NotTheSame@different.com'
        )
        other_cart_product = self.create_cart_product(
            product=self.create_product(create_valid_product=True),
            cart=other_user.cart,
        )
        db.session.add(other_user)
        db.session.add(other_cart_product)
        db.session.add(user)
        db.session.add(cart_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=user.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['id'], cart_product.id)
