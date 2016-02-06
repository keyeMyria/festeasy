from flask import request
from flask_restful import Resource

from backend import db
from backend.models import Package
from backend.api.utils import get_or_404
from backend.api.v1.schemas import PackageSchema


package_schema = PackageSchema()


class PackageSingleton(Resource):
    def get(self, package_id):
        package = get_or_404(Package, Package.id == package_id)
        return package_schema.dump(package).data
