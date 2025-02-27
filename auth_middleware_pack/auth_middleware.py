from django.http import JsonResponse
from myapp.middlewares.auth_middleware_pack.separate_path import separate_path_func
from api.jwt_token_api.jwt_token import JwtToken
from myapp.middlewares.auth_middleware_pack.add_user_id import add_user_id_func


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if separate_path_func(request=request):
            return self.get_response(request)
        jwt_token = request.headers.get("Authorization")
        if not JwtToken.validate(token=jwt_token):
            return JsonResponse({
                "ok": False,
            }, status=401)
        request.POST = add_user_id_func(request=request)
        response = self.get_response(request)
        return response
