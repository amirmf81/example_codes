from django.http import JsonResponse

from myapp.models.user_model import User
from api.register_api.second_step.make_otp import make_otp_func
from api.register_api.change_register_state import change_register_state_func
from api.phone_number_api.phone_number import PhoneNumberHandler


def second_register_func(phone_number, user_id):
    state = PhoneNumberHandler(phone_number=phone_number).validate()
    if state == 0:
        return make_otp_func(phone_number=phone_number, user_id=user_id)

    elif state == 1:
        return JsonResponse({
            "ok": False,
            "errors": "phone number is not correct",
        })
    else:
        return JsonResponse({
            "ok": False,
            "errors": "this phone number has been used before",
        })
