from django.core.exceptions import ObjectDoesNotExist

from api.jwt_token_api.jwt_token import JwtToken
from api.register_api.register_handler import register_handler_func


def complete_register_view_func(request):
    user_id = request.POST.get("user_id")
    return register_handler_func(request=request, user_id=user_id)
