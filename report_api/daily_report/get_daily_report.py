from datetime import date
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from myapp.models.location_model import Location
from api.calculate_distance_api.get_total_distance import get_total_distance_func
from api.event_api_2.event_handler.all_event_handler import EventHandler
from myapp.models.daily_report_model import DailyReport


class DailyReportHandler:
    def __init__(self, car_id):
        self.car_id = car_id

    def start(self):
        daily_report = DailyReport(
            car_id=self.car_id,
            speed_distance=self.get_speed_distance(),
            speed_time=self.get_speed_time(),
            acceleration_distance=self.get_acceleration_distance(),
            acceleration_time=self.get_acceleration_time(),
            location_time=self.get_location_time(),
            total_distance=self.get_total_distance(),
            total_time=self.get_total_time(),
        )
        daily_report.create()
        return DailyReportHandler(car_id=self.car_id).response(daily_report=daily_report)

    def get_speed_distance(self):
        return EventHandler.get_distance(car_id=self.car_id, field="speed", day=date.today())

    def get_speed_time(self):
        return EventHandler.get_time(car_id=self.car_id, field="speed", day=date.today())

    def get_acceleration_distance(self):
        return EventHandler.get_distance(car_id=self.car_id, field="acceleration", day=date.today())

    def get_acceleration_time(self):
        return EventHandler.get_time(car_id=self.car_id, field="acceleration", day=date.today())

    def get_location_time(self):
        return EventHandler.get_time(car_id=self.car_id, field="location", day=date.today())

    def get_total_distance(self):
        return get_total_distance_func(car_id=self.car_id, day=date.today())

    def get_total_time(self):
        total_time = 0.0
        locations = Location.get_all_locations(car_id=self.car_id)
        for location_place in range(0, len(locations)):
            if locations[location_place].date.date() == date.today() and location_place + 1 < len(locations):
                first_location = locations[location_place]
                second_location = locations[location_place + 1]
                total_time += divmod((second_location.date - first_location.date).total_seconds(), 1)[0]
        return total_time

    @classmethod
    def response(cls, daily_report: DailyReport):
        try:
            return JsonResponse({
                "car_id": daily_report.car_id,
                "distance in dangerous speed zone": daily_report.speed_distance,
                "time in dangerous speed zone": daily_report.speed_time,
                "distance in dangerous acceleration zone": daily_report.acceleration_distance,
                "time in dangerous acceleration zone": daily_report.acceleration_time,
                "time in out of tehran": daily_report.location_time,
                "total distance": daily_report.total_distance,
                "total time": daily_report.total_time,
            })
        except ObjectDoesNotExist:
            return JsonResponse({
                "ok": False,
                "errors": "this car does not exist",

            })
