from rest_framework import generics
from ..models import Car
from .serializers import CarSerializer
from django.views.generic import TemplateView
from ..models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarModelSerializer, CarHomeSerializer
from django.urls import reverse_lazy


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # def get_success_url(self):
    #     return reverse_lazy("home")


class CarFormView(TemplateView):
    template_name = "add_car.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["car_marka_opts"] = CarBrand.objects.all()

        context["other_data"] = "Some additional data"

        return context


class BrandModelsAPIView(APIView):
    def get(self, request, brand_name):
        try:
            brand = CarBrand.objects.get(name=brand_name)
        except CarBrand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=404)

        models = CarModel.objects.filter(brand=brand)
        serializer = CarModelSerializer(models, many=True)
        return Response(serializer.data)


class HomeAPIView(APIView):
    def get(self, request):
        # Tüm arabaları alıyoruz
        cars = Car.objects.all()

        # Arabaları serileştiriyoruz
        serializer = CarHomeSerializer(cars, many=True)

        # JSON olarak geri döndürüyoruz
        return Response(serializer.data)
