from api.location_api.location_handler import location_handler_func
from myapp.models.location_model import Location


def get_location_view_func(request):
    car_id = request.POST.get("car_id")
    speed = request.POST.get("speed")
    acceleration = request.POST.get("acceleration")
    latitude = request.POST.get("latitude",)
    longitude = request.POST.get("longitude")
    user_id = request.POST.get("user_id")
#    print(f"car_id{car_id}*")
    return location_handler_func(
        user_id=user_id,
        car_id=car_id,
        speed=speed,
        acceleration=acceleration,
        latitude=latitude,
        longitude=longitude,
    )
