from flask import url_for

from backend import db
from backend.testing import APITestCase, factories
from backend.models import PackagedStockUnit


endpoint = 'v1.packagedstockunitsingleton'


class TestPackagedStockUnitSingleton(APITestCase):
    def test_delete(self):
        psu = factories.PackagedStockUnitFactory()
        db.session.add(psu)
        db.session.commit()
        repsonse = self.api_request(
            'delete',
            url_for(endpoint, packaged_stock_unit_id=psu.id),
        )
        self.assertEqual(repsonse.status_code, 200, repsonse.json)
        fetched_PSUs = PackagedStockUnit.query.all()
        self.assertEqual(fetched_PSUs, [])
