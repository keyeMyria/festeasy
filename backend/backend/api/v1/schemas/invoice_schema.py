from marshmallow import fields

from . import EntitySchema


class InvoiceSchema(EntitySchema):
    order_id = fields.Integer()
    # order = fields.Nested(OrderSchema)
    total_rands = fields.Float()
    amount_due_rands = fields.Float()
