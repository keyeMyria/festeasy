from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.changepassword'


class TestChangePassword(APITestCase):
    def test_correct_password(self):
        data = {
            'current_password': '123',
            'new_password': '456',
        }
        user = factories.UserFactory(
            password=data['current_password'],
        )
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'post',
            url_for(endpoint, user_id=user.id),
            data=data,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(user.has_password(data['current_password']))
        self.assertTrue(user.has_password(data['new_password']))

    def test_incorrect_password(self):
        current_password = 'a'
        user = factories.UserFactory(
            password=current_password,
        )
        db.session.add(user)
        db.session.commit()
        data = {
            'current_password': current_password + 'incorrect stuff',
            'new_password': 'anything',
        }
        response = self.api_request(
            'post',
            url_for(endpoint, user_id=user.id),
            data=data,
        )
        self.assertEqual(response.status_code, 401)
        self.assertTrue(user.has_password(current_password))
