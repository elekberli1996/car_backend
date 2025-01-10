from rest_framework import serializers
from ..models import Car, CarImage, CarModel


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["image"]


class CarSerializer(serializers.ModelSerializer):
    car_images = CarImageSerializer(many=True, required=False)

    class Meta:
        model = Car
        fields = [
            "brand",
            "model",
            "vehicle_type",
            "color",
            "fuel_type",
            "transmission",
            "mileage",
            "year",
            "price",
            "engine_size",
            "power",
            "vin",
            "currency",
            "unit",
            "information",
            "name",
            "tel",
            "city",
            "main_img",
            "car_images",
        ]

    def create(self, validated_data):
        car_images_data = validated_data.pop("car_images", [])
        car = Car.objects.create(**validated_data)

        for image_data in car_images_data:
            CarImage.objects.create(car=car, **image_data)

        return car


class CarHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ["id", "name"]  # Modellerin ID ve adını döndür
