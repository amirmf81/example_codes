from datetime import date

from django.http import JsonResponse
from api.event_api_2.event_handler.all_event_handler import EventHandler


def get_report(car_id, field):
    distance = EventHandler.get_distance(car_id=car_id, field=field, day=date.today())
    print(date.today())
    time = EventHandler.get_time(car_id=car_id, field=field, day=date.today())
    return JsonResponse({
        "ok": True,
        "time": time,
        "distance": distance,
    })
