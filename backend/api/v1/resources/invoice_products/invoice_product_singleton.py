from flask_restful import Resource

from backend.models import InvoiceProduct
from backend.api.utils import get_or_404, marshal_or_fail
from backend.api.v1.schemas import InvoiceProductSchema


class InvoiceProductSingleton(Resource):
    def get(self, invoice_product_id):
        invoice_product = get_or_404(
            InvoiceProduct,
            InvoiceProduct.id == invoice_product_id,
        )
        return marshal_or_fail(
            'dump', invoice_product, InvoiceProductSchema())
