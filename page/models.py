import os, re
from django.db import models
from .utils.choices import *


def clean_string(value):
    return re.sub(r"[^a-zA-Z0-9_-]", "_", value)


def get_car_image_upload_to(instance, filename):
    folder_name = f"{instance.car.id}_{clean_string(instance.car.brand)}_{clean_string(instance.car.model)}"
    return os.path.join("car_images", folder_name, filename)


def get_main_image_upload_to(instance, filename):
    folder_name = (
        f"{instance.id}_{clean_string(instance.brand)}_{clean_string(instance.model)}"
    )
    return os.path.join("main_images", folder_name, filename)


class Car(models.Model):
    brand = models.CharField(
        max_length=50,
        # choices=BRAND_CHOICES
    )
    model = models.CharField(max_length=50)
    vehicle_type = models.CharField(
        max_length=20,
        # choices=VEHICLE_TYPE_CHOICES
    )
    color = models.CharField(max_length=30)
    fuel_type = models.CharField(
        max_length=20,
        #  choices=FUEL_TYPE_CHOICES
    )
    transmission = models.CharField(
        max_length=20,
        # choices=TRANSMISSION_CHOICES
    )
    mileage = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine_size = models.CharField(max_length=50)

    power = models.PositiveIntegerField()
    vin = models.CharField(max_length=50)
    currency = models.CharField(max_length=10, null=False, default="AZN")
    unit = models.CharField(max_length=10, null=False, default="KM")
    information = models.CharField(max_length=400)
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    main_img = models.ImageField(upload_to=get_main_image_upload_to, blank=True)
    # condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    # engine_displacement = models.CharField(max_length=7, choices=ENGINE_DISPLACEMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_created_at_date(self):
        return self.created_at.strftime("%d-%m-%Y")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_car_image_upload_to)

    def __str__(self):
        return f"Image for {self.car.brand} {self.car.model} {self.car.year}"


# ?-----------------


# Car Brand Model (e.g., BMW)
class CarBrand(models.Model):
    name = models.CharField(
        max_length=50, unique=True, blank=True
    )  # Brand name (BMW, Audi, etc.)

    def __str__(self):
        return self.name


# Car Model (Sub Models: X5, X6, X7, etc.)
class CarModel(models.Model):
    # Relationship with the Brand
    brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE, related_name="models", null=True, blank=True
    )
    name = models.CharField(
        max_length=100, blank=True, null=True
    )  # Model name (X5, X6, X7, etc.)

    def __str__(self):
        return f"{self.name}"
