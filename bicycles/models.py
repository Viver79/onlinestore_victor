from django.db import models
from os import path
from uuid import uuid4

# Create your models here.
class Bike_type(models.Model):
    title = models.CharField(max_length=50, unique=True)
    categories_bicycles = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Bike_brand(models.Model):
    title = models.CharField(max_length=50, unique=True)
    categories_bicycles = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Bike_size(models.Model):
    name = models.CharField(max_length=10, unique=True)
    categories_bicycles = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ProductBicycles(models.Model):

    def get_file_name_bicycles(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/bicycles', filename)

    titel = models.CharField(max_length=50, unique=True)
    titel_model = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    images = models.ImageField(upload_to=get_file_name_bicycles)
    bike_type = models.ForeignKey(Bike_type, on_delete=models.CASCADE)
    bike_brand = models.ForeignKey(Bike_brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('titel',)
        index_together = (('id', 'titel_model'))

    def __str__(self):
        return self.titel
