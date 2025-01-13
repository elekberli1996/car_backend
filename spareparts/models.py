import os,re
from django.db import models
# from .utils.choices import *


class Parts(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    part_name = models.CharField(max_length=50)
    cond = models.CharField(max_length=50, default="Yeni")
    price = models.IntegerField(null=True)
    currency = models.CharField(max_length=20, null=False, default="AZN")
    information = models.CharField(max_length=400)
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    main_img = models.ImageField(upload_to="main_part_images/", blank=True)
    created_at = models.DateField(auto_now_add=True)

    def get_created_at_date(self):
        return self.created_at.strftime("%d-%m-%Y")

    def __str__(self):
        return f"{self.brand} {self.model} "


class PartImage(models.Model):
    part = models.ForeignKey(Parts, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="other_part_images/")

    def __str__(self):
        return f"Image for {self.car.brand} {self.car.model} {self.part_name}"
