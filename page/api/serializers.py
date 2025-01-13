import django_filters
from rest_framework import serializers
from ..models import Car, CarImage, CarModel


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["image"]


class CarSerializer(serializers.ModelSerializer):
    car_images = serializers.ListField(child=serializers.ImageField(), required=False, write_only=True)
    created_at = serializers.SerializerMethodField()

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
            "created_at",

        ]

    def create(self, validated_data):
        request = self.context.get("request")
        car = Car.objects.create(**validated_data)
        car_images_data = request.FILES.getlist("car_images[]")

        if not car_images_data:
            raise serializers.ValidationError(
                {"car_images": "Resim dosyası yüklenmedi."}
            )

        try:
            for image_data in car_images_data:
                CarImage.objects.create(car=car, image=image_data)
        except Exception as e:
            raise serializers.ValidationError(
                {"car_images": f"Resim kaydedilirken hata oluştu: {str(e)}"}
            )

        return car

    def to_representation(self, instance):
        """Geri dönerken car_images'ı JSON formatında göster"""
        rep = super().to_representation(instance)
        rep["car_images"] = CarImageSerializer(instance.images.all(), many=True).data
        return rep
    
    def get_created_at(self, obj):
        return obj.get_created_at_date()


## <== home ==>
class CarHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


## <== home ==>
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ["id", "name"]  # Modellerin ID ve adını döndür


class CarFilter(django_filters.FilterSet):

    # Filtering options for price, year, and mileage
    # min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    # max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    # min_year = django_filters.NumberFilter(field_name="year", lookup_expr="gte")
    # max_year = django_filters.NumberFilter(field_name="year", lookup_expr="lte")
    # max_mileage = django_filters.NumberFilter(field_name="mileage", lookup_expr="lte")

    # Filtering options for categorical fields (must match database values exactly)
    # class Meta:
    # model = Car
    # fields = ["brand", "vehicle_type", "city", "color"]
    # Filters for brand, vehicle type, city, and color (exact match required)

    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    min_year = django_filters.NumberFilter(field_name="year", lookup_expr="gte")
    max_year = django_filters.NumberFilter(field_name="year", lookup_expr="lte")
    max_mileage = django_filters.NumberFilter(field_name="mileage", lookup_expr="lte")
    brand = django_filters.CharFilter(field_name="brand", lookup_expr="icontains")
    model = django_filters.CharFilter(field_name="model", lookup_expr="icontains")
    city = django_filters.CharFilter(field_name="city", lookup_expr="icontains")
    color = django_filters.CharFilter(field_name="color", lookup_expr="icontains")

    class Meta:
        model = Car
        fields = []
