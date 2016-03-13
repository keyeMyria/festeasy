from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import PackagedStockUnit


endpoint = 'v1.packagedstockunitcollection'


class TestPackagedStockUnitCollection(APITestCase):
    def test_get(self):
        psu = factories.PackagedStockUnitFactory()
        db.session.add(psu)
        db.session.commit()
        repsonse = self.api_request(
            'get',
            url_for(endpoint),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        self.assertEqual(repsonse.json[0]['id'], psu.id, repsonse.json)

    def test_post(self):
        package = factories.PackageFactory()
        su = factories.StockUnitFactory()
        db.session.add_all([package, su])
        db.session.commit()
        data = dict(
            package_id=package.id,
            stock_unit_id=su.id,
        )
        repsonse = self.api_request(
            'post',
            url_for(endpoint),
            data=data,
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        fetched_psu = PackagedStockUnit.query.first()
        self.assertIsNotNone(fetched_psu, repsonse.json)
        self.assertEqual(fetched_psu.package_id, package.id)
