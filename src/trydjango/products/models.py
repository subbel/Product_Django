from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title      = models.CharField(max_length=120)
    desciption = models.TextField(blank = True, null = True)
    price      = models.DecimalField(decimal_places=2, max_digits=10000)
    summary    = models.TextField()
    feature    = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f"/products/{self.id}"