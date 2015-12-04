from marshmallow import Schema, fields


class ChangePasswordSchema(Schema):
    current_password = fields.String()
    new_password = fields.String()

    class Meta:
        strict = True
