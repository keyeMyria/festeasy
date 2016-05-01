from marshmallow import fields

from . import EntitySchema
from .festival_schema import FestivalSchema
from .cart_product_schema import CartProductSchema


class CartSchema(EntitySchema):
    festival_id = fields.Integer()
    festival = fields.Nested(FestivalSchema())
    total_rands = fields.Float()
    cart_products = fields.Nested(CartProductSchema())
