import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from api.location_api.check_car_owner import check_car_owner_func
from api.location_api.location_scale_handler import location_scale_handler_func
from myapp.models.location_model import Location


def location_handler_func(user_id, car_id, speed, acceleration, latitude, longitude):
    try:
        if not check_car_owner_func(car_id=car_id, user_id=user_id):
            return JsonResponse({
                "ok": False,
                "errors": "this car does not belong to your company"
            })
        location = Location.create(
            car_id=car_id,
            speed=float(speed),
            acceleration=float(acceleration),
            latitude=float(latitude),
            longitude=float(longitude),
            date=datetime.datetime.now()
        )
        location.save()
        location_scale_handler_func(location=location)
        return JsonResponse({
            "ok": True,
        })

    except ValueError:
        return JsonResponse({
            "ok": False,
            "errors": "your data types are not correct",
        })
    except IntegrityError:
        return JsonResponse({
            "ok": False,
            "errors": "your fields could not be empty",
        })

    except ObjectDoesNotExist:
        return JsonResponse({
            "ok": False,
            "errors": "this car does not exist"
        })
