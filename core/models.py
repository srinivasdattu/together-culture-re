from django.contrib.auth.models import AbstractUser
from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_approved = models.BooleanField(default=False)
    is_admin_user = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)
    professional_background = models.TextField(blank=True)
    why_join = models.TextField(blank=True)
    how_contribute = models.TextField(blank=True)
