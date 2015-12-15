from flask import url_for

from backend import db
from backend.testing import APITestCase


endpoint = 'v1.invoiceproductsingleton'


class TestInvoiceProductSingleton(APITestCase):
    def test_get(self):
        invoice_product = self.create_invoice_product(
            unit_price_rands=11,
            product=self.create_product(create_valid_product=True),
            invoice=self.create_invoice(
                order=self.create_order(
                    festival=self.create_festival(
                        pre_populate=True,
                        name='asdf',
                        base_festival=self.create_base_festival(),
                    ),
                    user=self.create_user(normal_user=True, with_cart=True),
                ),
            ),
        )
        print(invoice_product.unit_price_rands)
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
