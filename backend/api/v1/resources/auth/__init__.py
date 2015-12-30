from backend.api.v1 import v1_api
from .signup import Signup
from .signin import Signin
from .reset_password import ResetPassword


v1_api.add_resource(Signup,
                    '/signup')
v1_api.add_resource(Signin,
                    '/signin')
v1_api.add_resource(ResetPassword,
                    '/reset-password')
