from flask import url_for

from backend import db
from backend.testing import APITestCase, factories


endpoint = 'v1.paymentsingleton'


class TestPaymentSingleton(APITestCase):
    def test_get(self):
        payment = factories.PaymentFactory()
        db.session.add(payment)
        db.session.commit()
        response = self.api_request(
            'get',
            url_for(endpoint, payment_id=payment.id),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], payment.id)
