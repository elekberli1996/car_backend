from ..models import *
from django.db import IntegrityError
from django.urls import reverse_lazy
from .serializers import CarSerializer, CarFilter
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import CarModelSerializer, CarHomeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# csrf korumasin  devre disi birakmak icin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class HomeAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarHomeSerializer(cars, many=True)
        return Response(serializer.data)


# @method_decorator(csrf_exempt, name="dispatch")
class CarCreateView(generics.CreateAPIView):
    # def post(self, request, *args, **kwargs):
    #     serializer = CarSerializer(data=request.data)

    #     if serializer.is_valid():
    #         try:
    #             car_instance = serializer.save()
    #             return Response(
    #                 {
    #                     "message": "Car added successfully",
    #                     "car": serializer.data,
    #                 },
    #                 status=status.HTTP_201_CREATED,
    #             )
    #         except IntegrityError:
    #             return Response(
    #                 {"error": "Database error. Please check unique constraints."},
    #                 status=status.HTTP_400_BAD_REQUEST,
    #             )
    #         except Exception as e:
    #             return Response(
    #                 {"error": f"Unexpected error: {str(e)}"},
    #                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #             )

    #     return Response(
    #         {"message": "Validation failed", "errors": serializer.errors},
    #         status=status.HTTP_400_BAD_REQUEST,
    #     )
    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            car_instance = serializer.save()
            return Response(
                {
                    "message": "Car added successfully",
                    "car_id": car_instance.id,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandModelsAPIView(APIView):
    def get(self, request, brand_name):
        try:
            brand = CarBrand.objects.get(name=brand_name)
        except CarBrand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=404)

        models = CarModel.objects.filter(brand=brand)
        serializer = CarModelSerializer(models, many=True)
        return Response(serializer.data)


class CarFilterView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CarFilter

    ordering_fields = ["price", "year", "mileage"]
    ordering = ["price"]


class CarFilterBrandAPIView(APIView):

    def get(self, request, brand, format=None):
        # Kullanıcının girdiği harfi içeren markaları bul
        cars = Car.objects.filter(brand__icontains=brand).prefetch_related(
            "images"
        )  # CarImage ile ilişkiyi önceden çek

        # Eğer marka bulunduysa, her aracı serialize et
        if cars.exists():
            # Serileştirilmiş araç verileri
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail": "No cars found for the selected brand."},
                status=status.HTTP_404_NOT_FOUND,
            )
