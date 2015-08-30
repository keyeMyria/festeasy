from flask import url_for

from backend import db
from backend.testing import APITestCase
from backend.models import InvoiceProduct


class TestInvoiceProductSingleton(APITestCase):
    def test_get(self):
        invoice_product = self.create_invoice_product(
            unit_price_rands=10,
            product=self.create_product(create_valid_product=True),
            invoice=self.create_invoice(
                order=self.create_order(
                    event=self.create_event(name='asdf'),
                    user=self.create_user(normal_user=True, with_cart=True),
                ),
            ),
        )
        db.session.add(invoice_product)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for('v1.invoiceproductsingleton', invoice_product_id=invoice_product.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], invoice_product.id)
