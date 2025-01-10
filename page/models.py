import os, re
from django.db import models
from .utils.choices import *


import os
import re


# Temizleme fonksiyonu
# def clean_string(value):
#     return re.sub(r"[^a-zA-Z0-9_-]", "_", value)


# Yükleme yolu fonksiyonu (Car resimleri için)
# def get_car_image_upload_to(instance, filename):
#     folder_name = (
#         f"{clean_string(instance.car.brand)}_{clean_string(instance.car.model)}"
#     )
#     return os.path.join(
#         "car_images", folder_name, filename
#     )  # Tüm resimler car_images klasörüne


# # Yükleme yolu fonksiyonu (Ana resim için)
# def get_main_image_upload_to(instance, filename):
#     folder_name = (
#         f"{clean_string(instance.car.brand)}_{clean_string(instance.car.model)}"
#     )
#     return os.path.join(
#         "main_images", folder_name, filename
#     )  # Ana resimler main_images klasörüne


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=20)
    transmission = models.CharField(max_length=20)
    mileage = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    price = models.IntegerField(null=True)
    engine_size = models.CharField(max_length=50)
    power = models.PositiveIntegerField()
    vin = models.CharField(max_length=50, unique=True)
    currency = models.CharField(max_length=20, null=False, default="AZN")
    unit = models.CharField(max_length=20, null=False, default="KM")
    information = models.CharField(max_length=400)
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    main_img = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateField(auto_now_add=True)

    def get_created_at_date(self):
        return self.created_at.strftime("%d-%m-%Y")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car_images/")

    def __str__(self):
        return f"Image for {self.car.brand} {self.car.model} {self.car.year}"


# ?-----------------
class CarBrand(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE, related_name="models", null=True, blank=True
    )
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
