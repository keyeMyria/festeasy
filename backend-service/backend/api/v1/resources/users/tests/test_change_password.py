from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.changepassword'


class TestChangePassword(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        self.user = self.session.user
        db.session.add(self.session)
        db.session.commit()

    def test_correct_password(self):
        data = {
            'current_password': '123',
            'new_password': '456',
        }
        self.user.set_password(data['current_password'])
        db.session.add(self.user)
        db.session.commit()
        response = self.api_request(
            'post',
            url_for(endpoint, user_id=self.user.id),
            data=data,
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertFalse(
            self.user.has_password(data['current_password']), response.json
        )
        self.assertTrue(self.user.has_password(data['new_password']), response.json)

    def test_incorrect_password(self):
        current_password = 'a'
        self.user.set_password(current_password)
        db.session.add(self.user)
        db.session.commit()
        data = {
            'current_password': current_password + 'incorrect stuff',
            'new_password': 'anything',
        }
        response = self.api_request(
            'post',
            url_for(endpoint, user_id=self.user.id),
            data=data,
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 400, response.json)
        self.assertTrue(self.user.has_password(current_password), response.json)
