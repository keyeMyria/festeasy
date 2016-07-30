from flask_restful import Resource

from backend.models import Invoice
from backend.api.utils import get_or_404
from backend.api.v1.schemas import InvoiceSchema


invoice_schema = InvoiceSchema()


class InvoiceSingleton(Resource):
    def get(self, invoice_id):
        invoice = get_or_404(Invoice, Invoice.id == invoice_id)
        return invoice_schema.dump(invoice).data
