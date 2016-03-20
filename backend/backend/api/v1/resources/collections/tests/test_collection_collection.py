from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import Collection


ENDPOINT = 'v1.collectioncollection'


class TestProductCollection(APITestCase):
    def test_get(self):
        collection = factories.CollectionFactory()
        db.session.add(collection)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(ENDPOINT),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json[0]['id'], collection.id, repsonse.json)

    def test_post(self):
        order = factories.OrderFactory()
        db.session.add(order)
        db.session.commit()
        data = dict(
            order_id=order.id,
        )
        repsonse = self.api_request(
            'post',
            url_for(ENDPOINT),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        fetched_collection = Collection.query.first()
        self.assertIsNotNone(fetched_collection, repsonse.json)
        self.assertEqual(fetched_collection.order_id, order.id, repsonse.json)
