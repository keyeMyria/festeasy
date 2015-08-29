from flask import url_for

from backend import db
from backend.testing import APITestCase


class TestUserResource(APITestCase):
    def test_get(self):
        user = self.create_user(normal_user=True, with_cart=True)
        db.session.add(user)
        db.session.commit()
        response = self.api_request(
            'get', 
            url_for('v1.userresource', user_id=user.id),
        )
        print(response.json)
        self.fail()