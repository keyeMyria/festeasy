from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import Product


endpoint = 'v1.packagesingleton'


class TestPackageSingleton(APITestCase):
    def test_get(self):
        package = factories.PackageFactory()
        db.session.add(package)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint, package_id=package.id),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json['id'], package.id, repsonse.json)
