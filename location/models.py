from django.conf import settings
from django.db import models


class City(models.Model):
    "Generated Model"
    city_id = models.IntegerField()
    city_title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )


# Create your models here.
