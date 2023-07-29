from django.db import models


# Create your models here.

class Tutorial(models.Model):
    objects = None
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)


class Employee(models.Model):
    objects = None
    firstName = models.CharField(max_length=70, blank=False, default='')
    lastName = models.CharField(max_length=200, blank=False, default='')
    email = models.CharField(max_length=50, blank=True, default='')
    mobile = models.CharField(max_length=10, blank=True, default='')

