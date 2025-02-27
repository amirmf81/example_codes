from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from myapp.models.user_model import User


def del_user_handler(user_id):
    try:
        User.del_user(user_id=user_id)
        return JsonResponse({
            "ok": True,
            "message": "user deleted successfully",
        })
    except ObjectDoesNotExist:
        return JsonResponse({
            "ok": False,
            "errors": "user does not exist",
        })
