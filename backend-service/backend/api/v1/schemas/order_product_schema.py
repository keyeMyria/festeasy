from marshmallow import fields

from . import EntitySchema
from .order_schema import OrderSchema
from .product_schema import ProductSchema


class OrderProductSchema(EntitySchema):
    unit_price_rands = fields.Float()
    quantity = fields.Integer()
    order = fields.Nested(OrderSchema)
    product = fields.Nested(ProductSchema)
