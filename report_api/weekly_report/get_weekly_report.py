import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from myapp.models.weekly_report_model import WeeklyReport
from myapp.models.daily_report_model import DailyReport


class WeeklyReportHandler:
    def __init__(self, car_id):
        self.car_id = car_id
        self.reports_list = self.get_daily_reports()

    def start(self):
        weekly_report = WeeklyReport(
            car_id=self.car_id,
            speed_distance=self.get_speed_distance(),
            speed_time=self.get_speed_time(),
            acceleration_distance=self.get_acceleration_distance(),
            acceleration_time=self.get_acceleration_time(),
            location_time=self.get_location_time(),
            total_distance=self.get_total_distance(),
            total_time=self.get_total_time(),
        )
        weekly_report.create()
        return WeeklyReportHandler(car_id=self.car_id).response(weekly_report=weekly_report)

    def get_daily_reports(self):
        this_date = datetime.datetime.now()
        week_time = 604800000
        all_reports = list(DailyReport.objects.filter(car_id=self.car_id))
        week_reports = []
        for report in all_reports:
            time_different = datetime.datetime.timestamp(datetime.datetime.now()) - datetime.datetime.timestamp(report.date)
            time_different *= 1000
            if time_different <= week_time:
                week_reports.append(report)
        return week_reports

    def get_speed_distance(self):
        ans = 0.0
        for report in self.reports_list:
            ans += report.speed_distance
        return ans

    def get_speed_time(self):
        ans = 0.0
        for report in self.reports_list:
            ans += report.speed_time
        return ans

    def get_acceleration_distance(self):
        ans = 0.0
        for report in self.reports_list:
            ans += report.acceleration_distance
        return ans

    def get_acceleration_time(self):
        ans = 0.0
        for report in self.reports_list:
            ans += report.acceleration_time
        return ans

    def get_location_time(self):
        ans = 0.0
        for report in self.reports_list:
            ans += report.location_time
        return ans

    def get_total_time(self):
        ans = 0.0
        for report in self.reports_list:
            ans += report.total_time
        return ans

    def get_total_distance(self):
        ans = 0.0
        for report in self.reports_list:
            ans += report.total_distance
        return ans

    @classmethod
    def response(cls, weekly_report: WeeklyReport):
        try:
            return JsonResponse({
                "car_id": weekly_report.car_id,
                "distance in dangerous speed zone": weekly_report.speed_distance,
                "time in dangerous speed zone": weekly_report.speed_time,
                "distance in dangerous acceleration zone": weekly_report.acceleration_distance,
                "time in dangerous acceleration zone": weekly_report.acceleration_time,
                "time in out of tehran": weekly_report.location_time,
                "total distance": weekly_report.total_distance,
                "total time": weekly_report.total_time,
            })
        except ObjectDoesNotExist:
            return JsonResponse({
                "ok": False,
                "errors": "this car does not exist",

            })
