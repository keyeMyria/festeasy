from factory import Factory, SubFactory

from backend.models import Invoice
from . import OrderFactory


class InvoiceFactory(Factory):
    class Meta:
        model = Invoice

    order = SubFactory(OrderFactory)
