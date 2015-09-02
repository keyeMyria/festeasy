from flask_restful import Resource

from backend.models import InvoiceProduct
from backend.api.utils import get_or_404
from backend.api.v1.schemas import InvoiceProductSchema


class InvoiceProductSingleton(Resource):
    def __init__(self):
        self.invoice_product_schema = InvoiceProductSchema()

    def get(self, invoice_product_id):
        invoice_product = get_or_404(
            InvoiceProduct,
            InvoiceProduct.id == invoice_product_id,
        )
        data, errors = self.invoice_product_schema.dump(invoice_product)
        return data
