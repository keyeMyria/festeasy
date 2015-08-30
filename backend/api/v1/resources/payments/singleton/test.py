from flask import url_for

from backend import db
from backend.testing import APITestCase


class TestPaymentSingleton(APITestCase):
    def test_get(self):
        payment = self.create_payment(
            invoice=self.create_invoice(
                order=self.create_order(
                    event=self.create_event(name='asd'),
                    user=self.create_user(normal_user=True, with_cart=True),
                ),
            ),
            amount_rands=19,
        )
        db.session.add(payment)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for('v1.paymentsingleton', payment_id=payment.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], payment.id)
