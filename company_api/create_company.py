from django.http import JsonResponse
from myapp.models.company_model import Company
from django.db import IntegrityError


def create_company_func(name, cars_number, owner_id):
    try:
        Company.create(
            name=name,
            cars_number=cars_number,
            owner_id=owner_id,
        )
        return JsonResponse({
            "ok": True,
            "message": "your company created successfully",
        })
    except IntegrityError:
        return JsonResponse({
            "ok": False,
            "errors": "this name has been used before",
        })
