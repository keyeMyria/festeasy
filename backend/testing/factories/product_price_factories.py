from factory import Factory

from backend.models import ProductPrice


class ProductPriceFactory(Factory):
    class Meta:
        model = ProductPrice

    amount_rands = 9.99
    info = None
