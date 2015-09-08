from marshmallow import fields, Schema


class SignupSchema(Schema):
    email_address = fields.Email()
    password = fields.String()
    first_name = fields.String()

    class Meta:
        strict = True
