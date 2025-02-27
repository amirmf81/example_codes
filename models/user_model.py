from django.db import IntegrityError
from django.db import models
import hashlib


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    register_state = models.IntegerField(default=0)

    @classmethod
    def create_user(cls, password, username):
        try:
            user = User(
                username=username,
                password=cls.hashing_password(password=password),
                register_state=1
            )
            user.save()

        except IntegrityError:
            raise IntegrityError

        except AttributeError:
            raise AttributeError

    @classmethod
    def hashing_password(cls, password):
        password_bytes = password.encode('utf-8')
        hashed_password = hashlib.sha256(password_bytes)
        return hashed_password.hexdigest()

    @classmethod
    def del_user(cls, user_id):
        user = User.objects.get(id=user_id)
        user.delete()

    @classmethod
    def save_state(cls, state, user_id):
        user = User.objects.get(id=user_id)
        user.register_state = state
        user.save()

    @classmethod
    def change_password(cls, new_password, user_id):
        user = User.objects.get(id=user_id)
        user.password = user.hashing_password(password=new_password)
        user.save()

    @classmethod
    def save_phone_number(cls, user_id, phone_number):
        user = User.objects.get(id=user_id)
        user.phone_number = phone_number
        user.save()
