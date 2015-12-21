from factory import Factory, SubFactory

from backend.models import CartProduct
from . import ProductFactory, CartFactory


class CartProductFactory(Factory):
    class Meta:
        model = CartProduct

    quantity = 1
    product = SubFactory(ProductFactory)
    cart = SubFactory(CartFactory)
