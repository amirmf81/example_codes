from django.http import JsonResponse
from redis import Redis
from api.scale_api.make_caching_scale import make_caching_scale_func
redis = Redis(host='localhost', port=6379, decode_responses=True)


def save_scale_func(user_id, speed_scale, acceleration_scale, location_scale, company_id):
    if company_id == "" or company_id is None:
        return JsonResponse({
            "ok": False,
            "errors": "company_id is not correct",
        })

    else:
        caching_scale = make_caching_scale_func(
            speed_scale=float(speed_scale),
            acceleration_scale=float(acceleration_scale),
            location_scale=location_scale,
        )
        redis.set(f"scale_{company_id}", caching_scale)
        return JsonResponse({
            "ok": True,
        })
