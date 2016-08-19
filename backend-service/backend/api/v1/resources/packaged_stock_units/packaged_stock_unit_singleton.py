from flask import request
from flask_restful import Resource

from backend import db
from backend.models import PackagedStockUnit
from backend.api.utils import get_or_404
from backend.api.v1.schemas import PackagedStockUnitSchema


psu_schema = PackagedStockUnitSchema()


class PackagedStockUnitSingleton(Resource):
    def delete(self, packaged_stock_unit_id):
        psu = get_or_404(PackagedStockUnit,
            PackagedStockUnit.id == packaged_stock_unit_id)
        db.session.delete(psu)
        db.session.commit()
        return
