from marshmallow import fields

from backend.api.utils import EntitySchema


class SessionSchema(EntitySchema):
    token = fields.String(dump_only=True)
    user_id = fields.Integer()

    class Meta:
        strict = True


class NormalUserSessionSchema(SessionSchema):
    expires_on = fields.DateTime(dump_only=True)


class AdminUserSessionSchema(SessionSchema):
    expires_on = fields.DateTime()


def get_appropriate_user_schema(request):
    return NormalUserSessionSchema()
