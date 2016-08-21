from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import User


endpoint = 'v1.usersingleton'


class TestUserSingleton(APITestCase):
    def setUp(self):
        super().setUp()
        self.user = factories.UserFactory()
        self.session = factories.SessionFactory(user=self.user)
        db.session.add_all([self.user, self.session])
        db.session.commit()

    def test_get(self):
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=self.user.id),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], self.user.id, response.json)

    def test_patch(self):
        data = dict(
            first_name='b',
        )
        response = self.api_request(
            'patch',
            url_for(endpoint, user_id=self.user.id),
            data=data,
            session_token=self.session.token,
        )
        fetched_user = User.query.one()
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(
            fetched_user.first_name,
            data['first_name'],
            response.json,
        )
        self.assertEqual(response.json['id'], self.user.id, response.json)
