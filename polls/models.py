from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class RusWord(models.Model):
    value = models.TextField(null=False, default='')


class EnWord(models.Model):
    value = models.TextField(null=False, default='')
    id_rus = models.ManyToManyField('RusWord')
