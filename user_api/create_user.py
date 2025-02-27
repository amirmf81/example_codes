from django.http import JsonResponse
from django.db import IntegrityError
from api.register_api.change_register_state import change_register_state_func
from myapp.models.user_model import User


def create_user_func(username, password):
 #   errors = []
 #   if username is None:
 #       errors.append("username is required")
 #   if password is None:
 #       errors.append("password is required")
 #   if errors:
 #       return JsonResponse({
  #          "ok": False,
  #          "errors": errors,
  #      })

    try:
        User.create_user(username=username, password=password)
        user_id = User.objects.get(username=username).id
        change_register_state_func(user_id=user_id, new_state=1)
        return JsonResponse({
            "ok": True
        })

    except IntegrityError:
        return JsonResponse({
            "ok": False,
            "error": "this username has been used before",
        })

    except AttributeError:
        return JsonResponse({
            "ok": False,
            "error": "username or password is to long",
        })
