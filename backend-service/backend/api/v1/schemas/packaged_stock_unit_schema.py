from marshmallow import fields

from . import EntitySchema, StockUnitSchema
from .package_schema import PackageSchema


class PackagedStockUnitSchema(EntitySchema):
    stock_unit_id = fields.Integer()
    stock_unit = fields.Nested(StockUnitSchema)
    package_id = fields.Integer()
    package = fields.Nested(PackageSchema)
