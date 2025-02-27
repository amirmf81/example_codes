from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from myapp.models.user_model import User


def get_state_func(user_id):
    try:
        state = User.objects.get(id=user_id).register_state
        return JsonResponse({
            "ok": True,
            "state": state,
        })

    except ObjectDoesNotExist:
        return JsonResponse({
            "ok": False,
            "errors": "this user does not exist",
        })