from backend.api.v1 import v1_api
from .signup import Signup
from .signin import Signin
from .facebook import Facebook
from .reset_password import ResetPassword


v1_api.add_resource(Signup,
                    '/auth/signup')
v1_api.add_resource(Signin,
                    '/auth/signin')
v1_api.add_resource(ResetPassword,
                    '/auth/reset-password')
v1_api.add_resource(Facebook,
                    '/auth/facebook')
