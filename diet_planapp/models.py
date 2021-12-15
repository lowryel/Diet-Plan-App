from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class fill_formModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=User)
    age = models.IntegerField(blank=False)
    height = models.FloatField(blank=False)
    weight = models.FloatField(blank=False)
    weekly_budget = models.IntegerField(blank=False)
    gender = models.CharField(max_length=50, blank=False)
    lifestyle = models.CharField(max_length=50, blank=False)
    goals = models.CharField(max_length=50, blank=False)
    foods = models.CharField(max_length=50, blank=False)

