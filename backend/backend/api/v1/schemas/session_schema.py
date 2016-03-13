from marshmallow import fields

from . import EntitySchema


class SessionSchema(EntitySchema):
    token = fields.String()
    expires_on = fields.DateTime()
    user_id = fields.Integer()
