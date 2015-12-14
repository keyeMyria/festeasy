from marshmallow import fields

from backend.api.utils import EntitySchema
from . import ProductSchema


class CartProductSchema(EntitySchema):
    product_id = fields.Integer()
    cart_id = fields.Integer()
    sub_total_rands = fields.Float(dump_only=True)
    quantity = fields.Integer()
    product = fields.Nested(ProductSchema, dump_only=True)

    class Meta:
        strict = True
