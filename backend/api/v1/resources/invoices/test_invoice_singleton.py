from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.invoicesingleton'


class TestInvoiceSingleton(APITestCase):
    def test_get(self):
        invoice = factories.InvoiceFactory()
        db.session.add(invoice)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, invoice_id=invoice.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], invoice.id)
