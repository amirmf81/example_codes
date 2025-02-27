from redis import Redis
import random
import datetime
redis = Redis(host='localhost', port=6379, decode_responses=True)


class OTP:
    def __init__(self, phone_number, user_id):
        self.user_id = user_id
        self.phone_number = phone_number
        self.time = datetime.datetime.now()
        self.otp = ""

    def generate_otp(self):
  #      print(redis.get(f"otp_{self.user_id}"))
#            should wait 5 min
        for i in range(0, 6):
            self.otp += str(random.randint(0, 9))
     #   return self.otp

    def save_otp(self):
        data = {
            "otp": self.otp,
            "user_id": self.user_id,
            "phone_number": self.phone_number,
            "time": self.time
        }
        str_data = str(data)
        redis.set(f'otp_{self.user_id}', str_data, ex=300)
#        expired_time = datetime.timedelta(seconds=300)
#        set expired time

    @classmethod
    def estimated_time(cls, user_id):
        time = eval(redis.get(f'otp_{user_id}'))["time"]
        this_time = datetime.datetime.now()
        return 300 - int((this_time - time).total_seconds())

    @classmethod
    def not_generated(cls, user_id):
        if redis.get(f'otp_{user_id}') is None:
            return True
        return False

    @classmethod
    def del_otp(cls):
        pass
