from api.report_api.weekly_report.get_weekly_report import WeeklyReportHandler


def weekly_report_view_func(request):
    car_id = request.POST.get("car_id")
    return WeeklyReportHandler(car_id=car_id).start()
