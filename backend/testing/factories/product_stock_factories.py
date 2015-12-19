from factory import Factory, SubFactory

from backend.models import ProductStock
from . import ProductFactory, SupplierFactory


class ProductStockFactory(Factory):
    class Meta:
        model = ProductStock

    product = SubFactory(ProductFactory)
    supplier = SubFactory(SupplierFactory)
    cost_rands = 10
