from marshmallow import fields

from . import EntitySchema
from .festival_schema import FestivalSchema
from .invoice_schema import InvoiceSchema


class OrderSchema(EntitySchema):
    festival_id = fields.Integer()
    festival = fields.Nested(FestivalSchema)
    current_invoice = fields.Nested(InvoiceSchema)
    user_id = fields.Integer()
    total_rands = fields.Float()
    shipping_address = fields.String()
