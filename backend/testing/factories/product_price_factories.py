from factory import Factory, SubFactory

from backend.models import ProductPrice
from . import ProductFactory


class ProductPriceFactory(Factory):
    class Meta:
        model = ProductPrice

    amount_rands = 9.99
    notes = None
    product = SubFactory(ProductFactory)
