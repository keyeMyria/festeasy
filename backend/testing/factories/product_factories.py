from factory import Factory

from backend.models import Product


class ProductFactory(Factory):
    class Meta:
        model = Product

    name = 'Chicken'
    description = 'This is some chicken.'
    is_enabled = True
    cost_rands = 9.99
    price_rands = 12.99
