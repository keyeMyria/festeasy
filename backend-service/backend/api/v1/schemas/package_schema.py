from marshmallow import fields

from . import EntitySchema, OrderSchema


class PackageSchema(EntitySchema):
    order = fields.Nested(OrderSchema)
    order_id = fields.Integer()
