from django.http import JsonResponse

from api.scale_api.save_scale import save_scale_func


def get_scale_view_func(request):
    user_id = request.POST.get("user_id")
    company_id = request.POST.get("company_id")
    speed_scale = request.POST.get("speed_scale")
    acceleration_scale = request.POST.get("acceleration_scale")
    location_scale = request.POST.get("location_scale")
    return save_scale_func(
        user_id=user_id,
        speed_scale=speed_scale,
        acceleration_scale=acceleration_scale,
        location_scale=location_scale,
        company_id=company_id,
    )
