from django.db import models, IntegrityError
from myapp.models.user_model import User


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cars_number = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def create(cls, name, cars_number, owner_id):
        try:
            company = Company(
                name=name,
                cars_number=cars_number,
                owner=User.objects.get(id=owner_id),
            )
            company.save()
        except IntegrityError:
            raise IntegrityError

    @classmethod
    def delete_comp(cls, comp_id):
        company = Company.objects.get(id=comp_id)
        company.delete()


