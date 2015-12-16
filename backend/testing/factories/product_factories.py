from factory import Factory, SubFactory

from backend.models import Product
from . import ProductPriceFactory


class ProductFactory(Factory):
    class Meta:
        model = Product

    name = 'Chicken'
    description = 'This is some chicken.'
    is_enabled = True
    cost_rands = 9.99
    product_prices = SubFactory(ProductPriceFactory)
