from django.db.models import ObjectDoesNotExist
from django.http import JsonResponse

from api.jwt_token_api.jwt_token import JwtToken
from myapp.models.user_model import User


def login_handler(username, password):
  #  errors = []
  #  if username is None:
  #      errors.append("username is required")
  #  if password is None:
  #      errors.append("password is required")
  #  if errors:
  #      return JsonResponse({
  #          "ok": False,
  #          "errors": errors,
  #      })

    try:
        user = User.objects.get(username=username, password=User.hashing_password(password=password))
        return JsonResponse({
            "ok": True,
            "token": JwtToken.generate(user=user),
        })

    except ObjectDoesNotExist:
        return JsonResponse({
            "ok": False,
            "errors": "username or password is wrong",
        }, status=403)
