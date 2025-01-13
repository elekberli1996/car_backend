import django_filters
from rest_framework import serializers
from ..models import *


class PartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartImage
        fields = ["image"]


class PartSerializer(serializers.ModelSerializer):
    part_images = serializers.ListField(
        child=serializers.ImageField(), required=False, write_only=True
    )

    class Meta:
        model = Parts
        fields = [
            "brand",
            "model",
            "part_name",
            "cond",
            "price",
            "currency",
            "information",
            "name",
            "tel",
            "city",
            "main_img",
            "part_images",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        part = Parts.objects.create(**validated_data)
        part_images_data = request.FILES.getlist("part_images[]")

        if not part_images_data:
            raise serializers.ValidationError(
                {"part_images": "Resim dosyası yüklenmedi."}
            )

        try:
            for image_data in part_images_data:
                PartImage.objects.create(part=part, image=image_data)
        except Exception as e:
            raise serializers.ValidationError(
                {"car_images": f"Resim kaydedilirken hata oluştu: {str(e)}"}
            )

        return part

    def to_representation(self, instance):
        """Geri dönerken car_images'ı JSON formatında göster"""
        rep = super().to_representation(instance)
        rep["part_images"] = PartImageSerializer(instance.images.all(), many=True).data
        return rep
