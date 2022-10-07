from .formData import strategyConfigFormApi
# from .auth import SignupApi, LoginApi
# from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
    api.add_resource(strategyConfigFormApi, '/api/strategy-config')
   