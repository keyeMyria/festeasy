from marshmallow import fields

from .base_schema import BaseSchema


class EntitySchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    created_on = fields.DateTime(dump_only=True)
    last_updated_on = fields.DateTime(dump_only=True)
