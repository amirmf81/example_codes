from api.report_api.get_report import get_report


def report_view_func(request):
    car_id = request.POST.get("car_id")
    field = request.POST.get("field")
    return get_report(car_id=car_id, field=field)
