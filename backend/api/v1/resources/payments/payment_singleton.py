from flask_restful import Resource

from backend.models import Payment
from backend.api.utils import get_or_404
from backend.api.v1.schemas import PaymentSchema


payment_schema = PaymentSchema()


class PaymentSingleton(Resource):
    def get(self, payment_id):
        payment = get_or_404(Payment, Payment.id == payment_id)
        return payment_schema.dump(payment).data
