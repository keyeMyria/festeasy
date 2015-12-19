from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.festivalsingleton'


class TestFestivalSingleton(APITestCase):
    def test_get(self):
        festival = factories.FestivalFactory()
        db.session.add(festival)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, festival_id=festival.id),
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['id'], festival.id, response.json)

    def test_patch(self):
        new_name = 'aaa'
        festival = factories.FestivalFactory()
        db.session.add(festival)
        db.session.commit()
        response = self.api_request(
            'patch',
            url_for(endpoint, festival_id=festival.id),
            data=dict(
                name=new_name,
            )
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(response.json['name'], new_name, response.json)
