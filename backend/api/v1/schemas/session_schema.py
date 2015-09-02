from marshmallow import fields

from backend.api.utils import EntitySchema


class SessionSchema(EntitySchema):
    token = fields.String()
    expires_on = fields.DateTime()
    user_id = fields.Integer()

    class Meta:
        strict = True
