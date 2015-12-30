from marshmallow import Schema, fields


class ResetPasswordSchema(Schema):
    token = fields.String()
    password = fields.String()

    class Meta:
        strict = True
