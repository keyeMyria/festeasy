from marshmallow import fields

from . import EntitySchema


class SupplierSchema(EntitySchema):
    name = fields.String()
    location = fields.String()
    contact_number = fields.String()
