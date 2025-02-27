from django.http import JsonResponse
from api.otp_api.otp_handler import OTP


def make_otp_func(phone_number, user_id):
    if OTP.not_generated(user_id=user_id):
        otp_object = OTP(phone_number=phone_number, user_id=user_id)
        otp_object.generate_otp()
        otp_object.save_otp()
        return JsonResponse({
            "ok": True,
            "otp": otp_object.otp,
        })
    else:
        return JsonResponse({
            "ok": False,
            "errors": f"you can ask again after {OTP.estimated_time(user_id=user_id)} seconds",
        })