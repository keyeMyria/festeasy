from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import Package


endpoint = 'v1.packagecollection'


class TestPackageCollection(APITestCase):
    def test_get(self):
        package = factories.PackageFactory()
        db.session.add(package)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json[0]['id'], package.id, repsonse.json)

    def test_post(self):
        order = factories.OrderFactory()
        db.session.add(order)
        db.session.commit()
        data = dict(
            order_id=order.id,
        )
        repsonse = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        fetched_package = Package.query.first()
        self.assertIsNotNone(fetched_package, repsonse.json)
        self.assertEqual(fetched_package.order_id, order.id)
