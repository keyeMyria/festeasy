from marshmallow import fields

from . import EntitySchema


class ProductSchema(EntitySchema):
    name = fields.String()
    price_rands = fields.Float()
    cost_rands = fields.Float(dump_only=True)
    description = fields.String()
    thumbnail_image_id = fields.Integer()
