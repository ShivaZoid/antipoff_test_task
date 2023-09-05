from django.db import models

from .validators import (validate_cadastre_number,
                         validate_latitude,
                         validate_longitude)


class Query(models.Model):
    cadastre_number = models.CharField(
        max_length=19,
        unique=True,
        validators=[validate_cadastre_number]
    )
    latitude = models.FloatField(validators=[validate_latitude])
    longitude = models.FloatField(validators=[validate_longitude])
    response = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)


class FakeServer(models.Model):
    run = models.BooleanField(default=False)
