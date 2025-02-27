import datetime

from django.http import JsonResponse
from redis import Redis
from api.register_api.change_register_state import change_register_state_func
from api.phone_number_api.save_phone_number import save_phone_number_func
redis = Redis(host='localhost', port=6379, decode_responses=True)


class ValidateOTP:

    @classmethod
    def validate(cls, otp, user_id):
        try:
            otp_object = eval(redis.get(f'otp_{user_id}'))
            time = otp_object["time"]
            if not cls.is_expired(time=time):
                user_otp = otp_object["otp"]
                if user_otp == otp:
                    change_register_state_func(user_id=user_id, new_state=2)
                    save_phone_number_func(phone_number=otp_object["phone_number"], user_id=user_id)
                    #save phone number
                    return JsonResponse({
                        "ok": True,
                    })
                else:
                    return JsonResponse({
                        "ok": False,
                        "errors": "otp is not correct",
                    })
            else:
                return JsonResponse({
                    "ok": False,
                    "errors": "otp is expired",
                })

        except:
            return JsonResponse({
                "ok": False,
                "errors": "otp is expired",
            })

    @classmethod
    def is_expired(cls, time):
        this_time = datetime.datetime.now()
        if (this_time - time).total_seconds() >= 120:
            return True
        return False
