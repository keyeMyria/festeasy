from marshmallow import fields

from backend.api.utils import EntitySchema


class SupplierSchema(EntitySchema):
    name = fields.String()
    location = fields.String()
    contact_number = fields.String()

    class Meta:
        strict = True
