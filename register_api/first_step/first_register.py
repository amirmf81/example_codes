from api.user_api.create_user import create_user_func
from api.register_api.first_step.validate.validate_password import validate_password_func
from django.http import JsonResponse
from api.register_api.first_step.validate.validate_username import validate_username_func


def first_register_handler(username, password):
    if not validate_username_func(username=username):
        return JsonResponse({
            "ok": False,
            "errors": "username only includes uppercase and lowercase letters and numbers and spaces"
        })
    if not validate_password_func(password=password):
        return JsonResponse({
            "ok": False,
            "errors": "password should have 6 characters at least and lowercase and uppercase letters and numbers and only includes uppercase and lowercase letters and numbers",
        })
    return create_user_func(username=username, password=password)
