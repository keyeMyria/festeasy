from marshmallow import fields

from . import EntitySchema


class InvoiceProductSchema(EntitySchema):
    order_id = fields.Integer()
    total_rands = fields.Float()
    amount_due_rands = fields.Float()
