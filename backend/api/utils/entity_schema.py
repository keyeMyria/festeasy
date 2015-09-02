from marshmallow import Schema, fields


class EntitySchema(Schema):
    id = fields.Integer(dump_only=True)
    created_on = fields.DateTime(dump_only=True)
    last_updated_on = fields.DateTime(dump_only=True)
