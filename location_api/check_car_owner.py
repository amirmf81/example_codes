from django.core.exceptions import ObjectDoesNotExist
from myapp.models.car_model import Car
from myapp.models.company_model import Company


def check_car_owner_func(car_id, user_id):
    try:
        company_id = Car.objects.get(id=car_id).owner.id
        if user_id == Company.objects.get(id=company_id).owner.id:
            return True
        return False

    except ValueError:
        raise ValueError

    except ObjectDoesNotExist:
        raise ObjectDoesNotExist
