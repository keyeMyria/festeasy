from factory import Factory, SubFactory

from backend.models import OrderProduct
from . import OrderFactory, ProductFactory


class OrderProductFactory(Factory):
    class Meta:
        model = OrderProduct

    unit_price_rands = 10
    quantity = 1
    order = SubFactory(OrderFactory)
    product = SubFactory(ProductFactory)
