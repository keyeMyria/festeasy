from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.changepassword'


class TestChangePassword(APITestCase):
    def test_correct_password(self):
        password_a = 'a'
        password_b = 'b'
        user = self.create_user(normal_user=True, with_cart=True)
        user.set_password(password_a)
        db.session.add(user)
        db.session.commit()
        data = {
            'current_password': password_a,
            'new_password': password_b,
        }
        response = self.api_request(
            'post',
            url_for(endpoint, user_id=user.id),
            data=data,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(user.has_password(password_a))
        self.assertTrue(user.has_password(password_b))

    def test_incorrect_password(self):
        password = 'a'
        user = self.create_user(normal_user=True, with_cart=True)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        data = {
            'current_password': password + 'incorrect stuff',
            'new_password': 'anything',
        }
        response = self.api_request(
            'post',
            url_for(endpoint, user_id=user.id),
            data=data,
        )
        self.assertEqual(response.status_code, 401)
        self.assertTrue(user.has_password(password))
