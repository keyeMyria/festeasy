from backend.api.v1 import v1_api
from .stock_unit_collection import StockUnitCollection


v1_api.add_resource(StockUnitCollection,
                    '/stock-units')
