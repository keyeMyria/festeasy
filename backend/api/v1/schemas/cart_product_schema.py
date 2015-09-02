from marshmallow import fields

from backend.api.utils import EntitySchema


class CartProductSchema(EntitySchema):
    product_id = fields.Integer()
    cart_id = fields.Integer()
    sub_total_rands = fields.Float()
    quantity = fields.Integer()

    class Meta:
        strict = True
