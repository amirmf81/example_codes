from api.event_api_2.send_event_2.send_all_event_2 import send_all_event_func
from api.find_city_api.find_city import is_in_tehran


def check_location_func(longitude, latitude, location_scale, car_id, location_id):
    if location_scale == "Yes":
        if not is_in_tehran(f"{latitude}, {longitude}"):
            send_all_event_func(car_id=car_id, location_id=location_id, field="location")
