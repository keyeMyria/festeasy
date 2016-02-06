from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Package
from backend.api.v1.schemas import PackageSchema


package_schema = PackageSchema()


class PackageCollection(Resource):
    def get(self):
        packages = Package.query.all()
        return package_schema.dump(packages, many=True).data

    def post(self):
        load_data = package_schema.load(request.get_json()).data
        package = None
        if load_data:
            package = Package(**load_data)
        else:
            package = Package()
        db.session.add(package)
        db.session.commit()
        return package_schema.dump(package).data
