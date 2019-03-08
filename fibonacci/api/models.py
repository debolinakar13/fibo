from __future__ import unicode_literals

from django.db import models

class Fibo(models.Model):

    number = models.IntegerField(null=True)
    result = models.TextField(null=True)
