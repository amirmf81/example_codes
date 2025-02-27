from api.jwt_token_api.jwt_token import JwtToken


def add_user_id_func(request):
 #   token = request.headers.get("Authorization")
    my_req = request.POST.copy()
    my_req["user_id"] = JwtToken.get_user_id(token=request.headers.get("Authorization"))
  #  print(token)
    return my_req
