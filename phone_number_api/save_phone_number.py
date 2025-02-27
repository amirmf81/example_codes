from django.http import JsonResponse
from myapp.models.user_model import User


def save_phone_number_func(phone_number, user_id):
    User.save_phone_number(user_id=user_id, phone_number=phone_number)
    return JsonResponse({
        "ok": True,
    })
