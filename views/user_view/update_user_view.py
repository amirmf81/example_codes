from api.user_api.update_password import update_password_func
from api.jwt_token_api.jwt_token import JwtToken


def update_view(request):
    new_password = request.POST.get("password")
#    user_id = JwtToken.get_user_id(token=request.headers.get("Authorization"))
    user_id = request.POST.get("user_id")
    print(user_id, new_password)
    return update_password_func(new_password=new_password, user_id=user_id)
