from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from api.register_api.first_step.validate.validate_password import validate_password_func
from myapp.models.user_model import User


def update_password_func(user_id, new_password):

    #"serializer check user_id and new password is not empty"
    if validate_password_func(password=new_password):
        try:
            User.change_password(new_password=new_password, user_id=user_id)
            return JsonResponse({
                "ok": True,
            })
        except ObjectDoesNotExist:
            return JsonResponse({
                "ok": False,
                "errors": "user does not exist",
            })
    else:
        return JsonResponse({
            "ok": False,
            "errors": "password is not valid",
        })
