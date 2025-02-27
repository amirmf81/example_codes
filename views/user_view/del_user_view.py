from api.jwt_token_api.jwt_token import JwtToken
from api.user_api.del_user import del_user_handler


def del_user_view_func(request):
    user_id = request.POST.get("user_id")
    return del_user_handler(user_id=user_id)

