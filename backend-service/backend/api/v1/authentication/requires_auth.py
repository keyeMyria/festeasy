import logging
from functools import wraps

from backend.exceptions import APIException

from .get_token_from_request import get_token_from_request
from .get_valid_session_from_token import get_valid_session_from_token


logger = logging.getLogger(__name__)


# TODO: Test.
# TODO: b64 stuffs.
# TODO: Create new exception for authentication.
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_from_request()
        if not token:
            logger.warning('No authentication token supplied.')
            raise APIException(
                message='No authentication token supplied.',
                status_code=401,
            )
        session = get_valid_session_from_token(token)
        return f(*args, authenticated_user=session.user, **kwargs)
    return decorated
