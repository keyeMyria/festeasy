from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.categorycollection'


class TestCategoryCollection(APITestCase):
    def test_get(self):
        category = self.create_category(name='Drinks')
        db.session.add(category)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]['name'], category.name)
