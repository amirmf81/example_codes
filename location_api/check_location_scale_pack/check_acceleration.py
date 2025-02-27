from api.event_api_2.send_event_2.send_all_event_2 import send_all_event_func


def check_acceleration_func(acceleration, acceleration_scale, car_id, location_id):
    if abs(acceleration) >= abs(acceleration_scale):
        send_all_event_func(location_id=location_id, car_id=car_id, field="acceleration")
