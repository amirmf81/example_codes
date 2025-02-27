from django.db import models
from myapp.models.location_model import Location
from myapp.models.car_model import Car


class Event(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    owner = models.ForeignKey(Car, on_delete=models.CASCADE)
    field = models.CharField(default=None)

    @classmethod
    def create(cls, owner_id, field, location_id):
        event = Event(
            location=Location.objects.get(id=location_id),
            owner=Car.objects.get(id=owner_id),
            field=field,
        )
        return event

    @classmethod
    def get_events(cls, car_id, field):
        car = Car.objects.get(id=car_id)
        return list(Event.objects.filter(owner=car, field=field))



