from marshmallow import fields

from backend.api.utils import EntitySchema


class InvoiceSchema(EntitySchema):
    order_id = fields.Integer()
    total_rands = fields.Float()
    amount_due_rands = fields.Float()

    class Meta:
        strict = True
