import logging
from datetime import datetime

from backend.models import Session
from backend.exceptions import APIException


logger = logging.getLogger(__name__)


# TODO: Test.
def get_valid_session_from_token(token):
    session = Session.query.filter(Session.token == token).one_or_none()

    if session is None:
        logger.warning('No session found with supplied token.')
        raise APIException(
            message='No session found with supplied token.',
            status_code=401,
        )

    if session.expires_on < datetime.utcnow():
        logger.warning('Session has expired.')
        raise APIException(
            message='Session has expired.',
            status_code=401,
        )
    return session
