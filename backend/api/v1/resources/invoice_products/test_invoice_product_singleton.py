from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.invoiceproductsingleton'


class TestInvoiceProductSingleton(APITestCase):
    def test_get(self):
        invoice_product = factories.InvoiceProductFactory()
        db.session.add(invoice_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint,
                    invoice_product_id=invoice_product.id
                    ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], invoice_product.id)
