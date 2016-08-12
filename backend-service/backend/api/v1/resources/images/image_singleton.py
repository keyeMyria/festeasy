from flask_restful import Resource

from backend.models import Image
from backend.api.utils import get_or_404
from backend.api.v1.schemas import ImageSchema


class ImageSingleton(Resource):
    def get(self, image_id):
        image = get_or_404(Image, Image.id == image_id)
        return ImageSchema().dump(image).data
