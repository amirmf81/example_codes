from django.db import models
from myapp.models.company_model import Company


class Car(models.Model):
    owner = models.ForeignKey(Company, on_delete=models.CASCADE)

    @classmethod
    def create(cls, owner_id):
        car = Car(
            owner=Company.objects.get(id=owner_id)
        )
        car.save()
