from marshmallow import fields

from . import EntitySchema


class ProductSchema(EntitySchema):
    name = fields.String()
    price_rands = fields.Float(dump_only=True)
    cost_rands = fields.Float(dump_only=True)
    description = fields.String()

    class Meta:
        strict = True
