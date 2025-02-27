from api.register_api.second_step.second_register import second_register_func


def second_register_handler_func(request, user_id):
    phone_number = request.POST.get("phone_number")
    # check phone number is not none
    return second_register_func(phone_number=phone_number, user_id=user_id)
