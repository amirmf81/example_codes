import datetime

import django.utils.timezone
from django.db import models, IntegrityError


class Location(models.Model):
    car_id = models.CharField(max_length=50, blank=False)
    speed = models.FloatField(null=False)
    acceleration = models.FloatField(null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    date = models.DateTimeField(null=False, default=django.utils.timezone.now())

    @classmethod
    def create(cls, car_id, speed, acceleration, latitude, longitude, date):
        try:
            if car_id == "":
                raise ValueError
            location = Location(
                car_id=car_id,
                speed=speed,
                acceleration=acceleration,
                latitude=latitude,
                longitude=longitude,
                date=date,
            )
            return location
        except ValueError:
            raise ValueError

        except IntegrityError:
            raise IntegrityError

    def save_location(self):
        self.save()

    @classmethod
    def get_all_locations(cls, car_id):
        return list(Location.objects.filter(car_id=car_id))
