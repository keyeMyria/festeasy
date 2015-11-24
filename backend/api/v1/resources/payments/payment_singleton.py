from flask_restful import Resource

from backend.models import Payment
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import PaymentSchema


class PaymentSingleton(Resource):
    def get(self, payment_id):
        payment = get_or_404(Payment, Payment.id == payment_id)
        return marshal_or_fail('dump', payment, PaymentSchema())
