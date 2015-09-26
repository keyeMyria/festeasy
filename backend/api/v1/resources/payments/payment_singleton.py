from flask_restful import Resource

from backend.models import Payment
from backend.api.utils import get_or_404
from backend.api.v1.schemas import PaymentSchema


class PaymentSingleton(Resource):
    def __init__(self):
        self.payment_schema = PaymentSchema()

    def get(self, payment_id):
        payment = get_or_404(Payment, Payment.id == payment_id)
        data, errors = self.payment_schema.dump(payment)
        return data
