from django.http import JsonResponse

from api.find_city_api.find_city import is_in_tehran


def check_city_view_func(request):
    latitude = request.POST.get("latitude")
    longitude = request.POST.get("longitude")
    return JsonResponse({
        "ok": is_in_tehran(f"{latitude}, {longitude}"),
    })
