from django.db import models

# Create your models here.


class AddOr(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True)
    number = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=50, blank=True)
    img = models.FileField(upload_to='docs/', blank=False)

    def __str__(self):
        return self.name


class AddRe(models.Model):
    locations = models.CharField(max_length=100, blank=True)
    detils = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    up_date = models.DateField(auto_now_add=True)
    success = models.BooleanField()
    name_g = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.detils

