from marshmallow import fields

from . import EntitySchema
from . import ProductSchema, SupplierSchema


class StockUnitSchema(EntitySchema):
    cost_rands = fields.Float(required=True)
    product_id = fields.Integer(required=True)
    product = fields.Nested(ProductSchema)
    supplier_id = fields.Integer(required=True)
    supplier = fields.Nested(SupplierSchema)

    class Meta:
        strict = True
