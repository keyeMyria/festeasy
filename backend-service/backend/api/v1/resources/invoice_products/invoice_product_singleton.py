from flask_restful import Resource

from backend.models import InvoiceProduct
from backend.api.utils import get_or_404
from backend.api.v1.schemas import InvoiceProductSchema
from backend.api.v1.authentication import requires_auth


invoice_product_schema = InvoiceProductSchema()


class InvoiceProductSingleton(Resource):
    method_decorators = [requires_auth]

    def get(self, invoice_product_id, authenticated_user):
        invoice_product = get_or_404(
            InvoiceProduct,
            InvoiceProduct.id == invoice_product_id,
        )
        return invoice_product_schema.dump(invoice_product).data
