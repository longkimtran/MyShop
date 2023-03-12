from django.db import models

# Create your models here.


class Features(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    feature_image = models.ImageField(null=True, blank=True, upload_to="images/")

class displayusers(models.Model):

    username = models.CharField(max_length=100)