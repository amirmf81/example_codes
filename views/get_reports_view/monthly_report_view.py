from api.report_api.monthly_report.get_monthly_report import MonthlyReportHandler


def monthly_report_view_func(request):
    car_id = request.POST.get("car_id")
    return MonthlyReportHandler(car_id=car_id).start()
