# from rest_framework import serializers
# from ..models import Car, CarImage


# class CarImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarImage
#         fields = ("id", "image", "description")


# class CarSerializer(serializers.ModelSerializer):
#     images = CarImageSerializer(many=True, required=False)

#     class Meta:
#         model = Car
#         fields = "__all__"

#     def create(self, validated_data):
#         images_data = self.context["request"].FILES.getlist("images")
#         car = Car.objects.create(**validated_data)

#         for image_data in images_data:
#             CarImage.objects.create(car=car, image=image_data)

#         return car

# ! Last version


from rest_framework import serializers
from ..models import Car, CarImage


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
            "unit",
            "year",
            "engine_size",
            "power",
            "vin",
            "currency",
            "information",
            "main_img",
            "car_images",
        ]

    def create(self, validated_data):
        car_images_data = validated_data.pop("car_images", [])
        car = Car.objects.create(**validated_data)

        for image_data in car_images_data:
            CarImage.objects.create(car=car, **image_data)

        return car



