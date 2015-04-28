from flask import make_response, jsonify
from werkzeug.exceptions import NotFound


def get_or_404(model, ident, message="No such entity found."):
    result = model.query.filter(model.id == ident).first()
    if result is None:
        raise NotFound(message, response=make_response(jsonify(message=message), 404))
    return result
