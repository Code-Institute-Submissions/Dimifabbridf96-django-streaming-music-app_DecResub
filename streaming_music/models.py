from django.db import models, db_table
from django.contrib.auth.models import User


class Audio_File(models.Model):
    audios = models.FileField(upload_to='media/')

    class Meta:
        ordering = ['audios']

