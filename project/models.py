from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Authentic(models.Model):
    list_type = [('superuser', 'superuser'), ('user', 'user'), ('admin', 'admin'),]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=list_type)

    def __str__(self):
        return self.user.username


class AddAc(models.Model):
    name = models.CharField(max_length=100, blank=False)
    detils = models.CharField(max_length=100, blank=True)
    locations = models.CharField(max_length=100, blank=True)
    worked = models.CharField(max_length=12, blank=True)
    up_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

