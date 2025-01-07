import os
from django.db import models
from .utils.choices import *

# Function to determine the upload path for car images
def get_car_image_upload_to(instance, filename):
    # Using the car's ID to create a folder for each car
    return os.path.join('car_images', str(instance.car.id), filename)


class Car(models.Model):
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=30)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    horsepower = models.PositiveIntegerField()
    engine_displacement = models.CharField(max_length=7, choices=ENGINE_DISPLACEMENT_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_car_image_upload_to)                # Specifying the folder path for the images
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.car.brand} {self.car.model} {self.car.year}"