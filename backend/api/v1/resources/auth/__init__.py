from backend.api.v1 import v1_api
from .signup import Signup
from .signin import Signin


v1_api.add_resource(Signup, '/signup')
v1_api.add_resource(Signin, '/signin')
