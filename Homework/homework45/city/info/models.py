from django.db import models


class City(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='city/images/')
    url = models.URLField()

# Create your models here.
