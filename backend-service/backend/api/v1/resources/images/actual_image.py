from flask import make_response
from flask_restful import Resource

from backend.models import Image
from backend.api.utils import get_or_404


class ActualImage(Resource):
    def get(self, image_id):
        image = get_or_404(Image, Image.id == image_id)
        response = make_response(image.file_data)
        response.headers['Content-Type'] = 'image/{0}'.format(image.filetype)
        return response
