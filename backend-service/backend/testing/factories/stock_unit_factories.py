from factory import Factory, SubFactory

from backend.models import StockUnit
from . import ProductFactory, SupplierFactory


class StockUnitFactory(Factory):
    class Meta:
        model = StockUnit

    product = SubFactory(ProductFactory)
    supplier = SubFactory(SupplierFactory)
    cost_rands = 10
