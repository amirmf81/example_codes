from api.register_api.third_step.third_register import third_register_func


def third_register_handler_func(request, user_id):
    company_name = request.POST.get("company_name")
    cars_number = int(request.POST.get("cars_number"))
    return third_register_func(company_name=company_name, cars_number=cars_number, user_id=user_id)
