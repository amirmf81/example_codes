from api.jwt_token_api.jwt_token import JwtToken
from api.user_api.get_state import get_state_func


def get_state_view_func(request):
    user_id = request.POST.get("user_id")
    return get_state_func(user_id=user_id)
