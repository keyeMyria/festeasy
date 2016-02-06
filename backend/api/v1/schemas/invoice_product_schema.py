from marshmallow import fields

from . import EntitySchema


class InvoiceProductSchema(EntitySchema):
    order_id = fields.Integer()
    unit_price_rands = fields.Float()
    quantity = fields.Integer()
    product_id = fields.Integer()
