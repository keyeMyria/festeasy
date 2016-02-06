from flask import request
from flask_restful import Resource

from backend import db
from backend.models import PackagedStockUnit
from backend.api.v1.schemas import PackagedStockUnitSchema


psu_schema = PackagedStockUnitSchema()


class PackagedStockUnitCollection(Resource):
    def get(self):
        psus = PackagedStockUnit.query.all()
        return psu_schema.dump(psus, many=True).data

    def post(self):
        load_data = psu_schema.load(request.get_json()).data
        psu = None
        if load_data:
            psu = PackagedStockUnit(**load_data)
        else:
            psu = PackagedStockUnit()
        db.session.add(psu)
        db.session.commit()
        return psu_schema.dump(psu).data
