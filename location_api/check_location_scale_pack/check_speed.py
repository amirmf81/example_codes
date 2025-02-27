from api.event_api.send_event.send_speed_event import SpeedEvent
from events import Dispatcher
from myapp.models.location_model import Location
from api.event_api_2.send_event_2.send_all_event_2 import send_all_event_func


def check_speed_func(speed, speed_scale, location_id, car_id):
    if speed >= speed_scale:
        send_all_event_func(location_id=location_id, car_id=car_id, field="speed")



#        location = Location.objects.get(id=location_id)
 #       print("**")
#        print(location)
 #       SpeedEvent.Dispatch(location)
#        event = Event(car_id=car_id)
 #       event.send_speed_event()
