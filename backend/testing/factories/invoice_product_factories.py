from factory import Factory, SubFactory

from backend.models import InvoiceProduct
from . import InvoiceFactory, ProductFactory


class InvoiceProductFactory(Factory):
    class Meta:
        model = InvoiceProduct

    unit_price_rands = 10
    product = SubFactory(ProductFactory)
    invoice = SubFactory(InvoiceFactory)
