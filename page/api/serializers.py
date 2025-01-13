import django_filters
from rest_framework import serializers
from ..models import Car, CarImage, CarModel


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["image"]


class CarSerializer(serializers.ModelSerializer):
    car_images = serializers.ListField(
        child=serializers.ImageField(), required=False, write_only=True
    )

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
        # Request'ten gelen veriyi alıyoruz
        request = self.context.get("request")

        # Tüm form verilerini yazdırma
        print("Form Verileri --------------------------->")
        print(request.data)  # Form verisi (string, sayılar vb.)

        # Dosya verilerini yazdırma
        if hasattr(request, "FILES"):
            print("Dosyalar --------------------------->")
            for key, file in request.FILES.items():
                print(f"{key}: {file.name} ({file.size} bytes)")

        # Car nesnesi oluşturuluyor
        car = Car.objects.create(**validated_data)

        car_images_data = (
            request.FILES.getlist("car_images[]") if hasattr(request, "FILES") else []
        )

        if car_images_data:
            try:
                for image_data in car_images_data:
                    print(f"Resim: {image_data.name}, Boyut: {image_data.size} bytes")
                    CarImage.objects.create(car=car, image=image_data)
                print("Resimler başarıyla kaydedildi.")
            except Exception as e:
                print(f"Resim kaydedilirken hata oluştu: {str(e)}")

        return car

    def to_representation(self, instance):
        """Geri dönerken car_images'ı JSON formatında göster"""
        rep = super().to_representation(instance)
        rep["car_images"] = CarImageSerializer(instance.images.all(), many=True).data
        return rep


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
    vehicle_type = django_filters.CharFilter(
        field_name="vehicle_type", lookup_expr="icontains"
    )
    city = django_filters.CharFilter(field_name="city", lookup_expr="icontains")
    color = django_filters.CharFilter(field_name="color", lookup_expr="icontains")

    class Meta:
        model = Car
        fields = []
