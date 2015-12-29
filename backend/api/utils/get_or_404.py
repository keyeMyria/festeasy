from sqlalchemy.orm import exc

from backend.api.v1.exceptions import APIException


def get_or_404(model, *criterion):
    try:
        return model.query.filter(*criterion).one()
    except exc.NoResultFound or exc.MultipleResultsFound:
        raise APIException(
            status_code=404,
            message="Entity not found.",
        )
