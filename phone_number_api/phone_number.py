from django.core.exceptions import ObjectDoesNotExist

from myapp.models.user_model import User


class PhoneNumberHandler:
    def __init__(self, phone_number):
        self.phone_number = phone_number
#        print(f"phone_number : {self.phone_number}")

    def validate(self) -> int:
        if not self.check_is_true():
            return 1
        elif not self.check_is_unique():
            return 2
        return 0

    def check_is_true(self):
        if len(self.phone_number) != 11:
            return False
        if self.phone_number[0] != '0':
            return False
        if self.phone_number[1] != '9':
            return False
        return True

    def check_is_unique(self):
        try:
            User.objects.get(phone_number=self.phone_number)
            return False
        except ObjectDoesNotExist:
            return True
