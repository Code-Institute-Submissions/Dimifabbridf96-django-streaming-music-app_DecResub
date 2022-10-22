from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)


    class Meta:
        ordering = ['name']

