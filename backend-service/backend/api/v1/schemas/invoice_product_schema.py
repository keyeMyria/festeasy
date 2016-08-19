from marshmallow import fields

from . import EntitySchema, ProductSchema


class InvoiceProductSchema(EntitySchema):
    order_id = fields.Integer()
    unit_price_rands = fields.Float()
    quantity = fields.Integer()
    sub_total_rands = fields.Float()
    product_id = fields.Integer()
    product = fields.Nested(ProductSchema())
