from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import Invoice
from backend.api.utils import get_or_404


singleton_fields = {
    'id': fields.Integer,
    'order_id': fields.Integer,
    'total_rands': fields.Float,
    'amount_due_rands': fields.Float,
}

class InvoiceSingleton(Resource):
    @marshal_with(singleton_fields)
    def get(self, invoice_id):
        invoice = get_or_404(Invoice, Invoice.id == invoice_id)
        return invoice
