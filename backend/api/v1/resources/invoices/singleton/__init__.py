from flask_restful import Resource

from backend.models import Invoice
from backend.api.utils import get_or_404
from backend.api.v1.schemas import InvoiceSchema


class InvoiceSingleton(Resource):
    def __init__(self):
        self.invoice_schema = InvoiceSchema()

    def get(self, invoice_id):
        invoice = get_or_404(Invoice, Invoice.id == invoice_id)
        data, errors = self.invoice_schema.dump(invoice)
        return data
