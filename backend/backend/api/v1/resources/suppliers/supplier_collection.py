from flask_restful import Resource

from backend.models import Supplier
from backend.api.v1.schemas import SupplierSchema


supplier_schema = SupplierSchema()


class SupplierCollection(Resource):
    def get(self):
        suplliers = Supplier.query.all()
        return supplier_schema.dump(suplliers, many=True).data
