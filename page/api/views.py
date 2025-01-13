from ..models import *
from drf_yasg import openapi
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.generic import TemplateView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import CarSerializer, CarFilter
from account.api.auth.security import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CarModelSerializer, CarHomeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

token_param = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    description="JWT Authorization header using the Bearer scheme. Example: 'Bearer <JWT token>'",
    type=openapi.TYPE_STRING,
)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def home_view(request):
    cars = Car.objects.all()
    serializer = CarHomeSerializer(cars, many=True)
    return Response(serializer.data)


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            car_instance = serializer.save()
            car_data = CarSerializer(car_instance).data
            return Response(
                {"message": "car added", "car_data": car_data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "pk"


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
        cars = Car.objects.filter(brand__icontains=brand).prefetch_related("images")

        if cars.exists():
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail": "No cars found for the selected brand."},
                status=status.HTTP_404_NOT_FOUND,
            )
