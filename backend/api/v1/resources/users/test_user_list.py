from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import User


class TestUserListResource(APITestCase):
    def test_get(self):
        user = self.create_user(normal_user=True, with_cart=True)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get', 
            url_for('v1.userlistresource'),
        )
        self.assertEqual(response.json[0]['id'], user.id)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        first_name = 'Test Name'
        email_address = 'a@b.c'
        password = '123'
        response = self.api_request(
            'post',
            url_for('v1.userlistresource'),
            data=dict(
                first_name=first_name,
                email_address=email_address,
                password=password,
            )
        )
        fetched_user = User.query.first()
        self.assertEqual(fetched_user.email_address, email_address)
        self.assertEqual(response.json['email_address'], email_address)
        self.assertEqual(response.status_code, 200)
