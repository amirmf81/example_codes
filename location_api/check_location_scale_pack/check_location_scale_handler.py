from api.location_api.check_location_scale_pack.check_location import check_location_func
from api.location_api.check_location_scale_pack.check_speed import check_speed_func
from api.location_api.check_location_scale_pack.check_acceleration import check_acceleration_func


def check_location_scale_handler_func(location, scales):
    check_speed_func(
        speed=location.speed,
        speed_scale=scales["speed_scale"],
        location_id=location.id,
        car_id=location.car_id,
    )
    check_acceleration_func(
        acceleration=location.acceleration,
        acceleration_scale=scales["acceleration_scale"],
        car_id=location.car_id,
        location_id=location.id,
    )
    check_location_func(
        longitude=location.longitude,
        latitude=location.latitude,
        location_scale=scales["location_scale"],
        car_id=location.car_id,
        location_id=location.id,
    )
