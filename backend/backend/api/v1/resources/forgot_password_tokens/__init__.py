from backend.api.v1 import v1_api
from .forgot_password_token_collection import ForgotPasswordTokenCollection

v1_api.add_resource(ForgotPasswordTokenCollection,
                    '/forgot-password-tokens')
