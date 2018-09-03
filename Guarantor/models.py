from django.db import models

# Create your models here.


class AddGu(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True)
    number = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=50, blank=True)
    img = models.FileField(upload_to='docs/', blank=False)
    work = models.CharField(max_length=100, blank=False)
    work_locations = models.CharField(max_length=100, blank=True)
    work_price = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

