from ..models import *
from django.db import IntegrityError
from django.urls import reverse_lazy
from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import CarModelSerializer, CarHomeSerializer


# csrf korumasin  devre disi birakmak icin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class HomeAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarHomeSerializer(cars, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class CarCreateView(generics.CreateAPIView):
    # queryset = Car.objects.all()
    # serializer_class = CarSerializer
    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            try:
                car_instance = serializer.save()
                return Response(
                    {
                        "message": "Car added successfully",
                        "car": serializer.data,  # Eklenen aracın tüm bilgilerini döndür
                    },
                    status=status.HTTP_201_CREATED,
                )
            except IntegrityError:
                return Response(
                    {"error": "Database error. Please check unique constraints."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Exception as e:
                return Response(
                    {"error": f"Unexpected error: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        # Daha açıklayıcı hata mesajları
        return Response(
            {"message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


# class CarFormView(TemplateView):
#     template_name = "add_car.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context["car_marka_opts"] = CarBrand.objects.all()

#         context["other_data"] = "Some additional data"

#         return context


class BrandModelsAPIView(APIView):
    def get(self, request, brand_name):
        try:
            brand = CarBrand.objects.get(name=brand_name)
        except CarBrand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=404)

        models = CarModel.objects.filter(brand=brand)
        serializer = CarModelSerializer(models, many=True)
        return Response(serializer.data)
