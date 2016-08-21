from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import User


endpoint = 'v1.usercollection'


class TestUserCollection(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        self.user = self.session.user
        db.session.add(self.session)
        db.session.commit()

    def test_get(self):
        response = self.api_request(
            'get',
            url_for(endpoint),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json[0]['id'], self.user.id, response.json)

    def test_post(self):
        first_name = 'Test Name'
        email_address = 'name@domain.com'
        password = '123'
        response = self.api_request(
            'post',
            url_for(endpoint),
            data=dict(
                first_name=first_name,
                email_address=email_address,
                password=password,
            ),
            session_token=self.session.token,
        )
        fetched_user = User.query.filter(User.email_address == email_address).one()
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(
            fetched_user.email_address,
            email_address,
            response.json,
        )
        self.assertEqual(
            response.json['email_address'],
            email_address,
            response.json,
        )
