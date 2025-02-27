from api.otp_api.validate_otp import ValidateOTP


def validate_otp_func(request):
    user_id = request.POST.get("user_id")
    otp = request.POST.get("otp")
    return ValidateOTP.validate(otp=otp, user_id=user_id)
