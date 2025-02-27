import datetime

import django.utils.timezone
from django.db import models
from myapp.models.daily_report_model import DailyReport


class MonthlyReport(models.Model):
    car_id = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(null=False, default=django.utils.timezone.now())
    speed_distance = models.FloatField(null=False, default=0)
    speed_time = models.FloatField(null=False, default=0)
    acceleration_distance = models.FloatField(null=False, default=0)
    acceleration_time = models.FloatField(null=False, default=0)
    location_time = models.FloatField(null=False, default=0)
    total_distance = models.FloatField(null=False, default=0)
    total_time = models.FloatField(null=False, default=0)

    def create(self):
        self.save()

