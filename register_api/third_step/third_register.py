from django.http import JsonResponse
from api.cars_api.create_car_pack.create_car import CreateCar
from api.company_api.create_company import create_company_func
from api.register_api.change_register_state import change_register_state_func
from myapp.models.company_model import Company
from api.register_api.third_step.validate_company_name.validate_name import validate_company_name_func
from api.register_api.third_step.validate_company_name.is_unique import is_unique_func
from django.db import IntegrityError


def third_register_func(company_name, cars_number, user_id):
#check name is not empty
    if not validate_company_name_func(name=company_name):
        return JsonResponse({
            "ok": False,
            "errors": "company name only include persian letters and spaces",
        })
    elif is_unique_func(name=company_name):
        response = create_company_func(name=company_name, cars_number=cars_number, owner_id=user_id)
        company_id = Company.objects.get(name=company_name).id
        CreateCar(cars_number=cars_number, owner_id=company_id).start()
        change_register_state_func(user_id=user_id, new_state=3)
        return response
    else:
        return JsonResponse({
            "ok": False,
            "errors": "this name has been used before",
        })


#make_cars
#validate_name
#create_company

