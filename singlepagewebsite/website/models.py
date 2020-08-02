from django.db import models


# Create your models here.

class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    services = models.CharField(max_length=260, unique=True)

    def __str__(self):
        return (self.services)

