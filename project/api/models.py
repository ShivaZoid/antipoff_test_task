from django.db import models


class QueryHistory(models.Model):
    cadastre_number = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    response = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
