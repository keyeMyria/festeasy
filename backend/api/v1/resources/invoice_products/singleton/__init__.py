from flask_restful import Resource, fields, marshal_with
from flask_restful import reqparse

from backend import db
from backend.models import InvoiceProduct
from backend.api.utils import get_or_404


user_fields = {
    'id': fields.Integer,
}

class InvoiceProductSingleton(Resource):
    @marshal_with(user_fields)
    def get(self, invoice_product_id):
        invoice_product = get_or_404(InvoiceProduct, InvoiceProduct.id == invoice_product_id)
        return invoice_product
