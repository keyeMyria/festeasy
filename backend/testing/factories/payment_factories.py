from factory import Factory, SubFactory

from backend.models import Payment
from . import InvoiceFactory


class PaymentFactory(Factory):
    class Meta:
        model = Payment

    amount_rands = 10
    invoice = SubFactory(InvoiceFactory)
