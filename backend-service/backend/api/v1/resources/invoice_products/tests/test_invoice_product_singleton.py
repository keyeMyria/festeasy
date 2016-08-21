from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.invoiceproductsingleton'


class TestInvoiceProductSingleton(APITestCase):
    def setUp(self):
        super().setUp()
        self.session = factories.SessionFactory()
        self.invoice_product = factories.InvoiceProductFactory(
            invoice=factories.InvoiceFactory(
                order=factories.OrderFactory(
                    user=self.session.user,
                )
            )
        )
        db.session.add_all([self.session, self.invoice_product])
        db.session.commit()

    def test_get(self):
        response = self.api_request(
            'get',
            url_for(
                endpoint,
                invoice_product_id=self.invoice_product.id
            ),
            session_token=self.session.token,
        )
        self.assertEqual(response.status_code, 200, response.json)
        self.assertEqual(
            response.json['id'],
            self.invoice_product.id,
            response.json,
        )
