from flask import url_for

from backend.utils import APITestCase


class TestUser(APITestCase):
    def test_create_user(self):
        email_address = 'test@festeasy.co.za'
        password = 'test_password'
        response = self.client.post(
            url_for('v1.create_user'), 
            data=dict(
                email_address=email_address, 
                password=password,
            )
        )
