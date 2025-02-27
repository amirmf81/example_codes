from api.report_api.daily_report.get_daily_report import DailyReportHandler


def daily_report_view_func(request):
    car_id = request.POST.get("car_id")
    return DailyReportHandler(car_id=car_id).start()
