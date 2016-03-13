from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.festivalcollection'


class TestFestivalCollection(APITestCase):
    def test_get(self):
        festival = factories.FestivalFactory()
        db.session.add(festival)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(
            response.json[0]['name'],
            festival.name,
            response.json,
        )
