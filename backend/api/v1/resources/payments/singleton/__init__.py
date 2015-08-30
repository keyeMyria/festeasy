from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import Payment
from backend.api.utils import get_or_404


singleton_fields = {
    'id': fields.Integer,
}

class PaymentSingleton(Resource):
    @marshal_with(singleton_fields)
    def get(self, payment_id):
        payment = get_or_404(Payment, Payment.id == payment_id)
        return payment
