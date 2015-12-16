from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import User


endpoint = 'v1.usersingleton'


class TestUserSingleton(APITestCase):
    def test_get(self):
        user = factories.UserFactory()
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, user_id=user.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], user.id)

    def test_patch(self):
        user = factories.UserFactory()
        data = dict(
            first_name='b',
        )
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for(endpoint, user_id=user.id),
            data=data,
        )
        fetched_user = User.query.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fetched_user.first_name, data['first_name'])
        self.assertEqual(response.json['id'], user.id)
