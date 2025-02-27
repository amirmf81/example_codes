from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from api.register_api.third_step.third_register_handler import third_register_handler_func
from myapp.models.user_model import User
from .second_step.second_register_handler import second_register_handler_func


def register_handler_func(request, user_id):
    try:
        state = User.objects.get(id=user_id).register_state
        if state == 1:
            return second_register_handler_func(request=request, user_id=user_id)
        elif state == 2:
            return third_register_handler_func(request=request, user_id=user_id)
        else:
            return JsonResponse({
                "ok": True,
                "message": "your register is completed",
            })


        #
        #other state


        #
    except ObjectDoesNotExist:
        return JsonResponse({
            "ok": False,
            "errors": "this user does not exist",
        })
