from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.categorycollection'


class TestCategoryCollection(APITestCase):
    def test_get(self):
        category = factories.CategoryFactory()
        db.session.add(category)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(
            response.json['data'][0]['name'],
            category.name,
            response.json,
        )
