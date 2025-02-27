from api.register_api.first_step.first_register import first_register_handler


def first_view_func(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    return first_register_handler(username=username, password=password)
