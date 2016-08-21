from flask import request
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser

from backend.models import InvoiceProduct
from backend.api.v1.schemas import InvoiceProductSchema
from backend.api.v1.authentication import requires_auth


query_args = {
    'invoice_id': fields.Integer(
        load_from='invoice-id',
        missing=None,
    )
}


# TODO: Test.
class InvoiceProductCollection(Resource):
    method_decorators = [requires_auth]

    def get(self, authenticated_user):
        params = parser.parse(query_args, request)
        invoice_id = params['invoice_id']
        q = InvoiceProduct.query
        if invoice_id:
            q = q.filter(InvoiceProduct.invoice_id == invoice_id)
        order_products = q.all()
        return InvoiceProductSchema().dump(order_products, many=True).data
