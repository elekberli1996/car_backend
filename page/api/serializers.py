from rest_framework import serializers
from ..models import Car, CarImage


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ("id", "image", "description")


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, required=False)

    class Meta:
        model = Car
        fields = "__all__"

    def create(self, validated_data):
        images_data = self.context["request"].FILES.getlist("images")
        car = Car.objects.create(**validated_data)

        for image_data in images_data:
            CarImage.objects.create(car=car, image=image_data)

        return car
