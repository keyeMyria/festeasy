from marshmallow import fields, Schema


class SigninSchema(Schema):
    email_address = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)

    class Meta:
        strict = True
