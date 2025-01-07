from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from ..models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    parser_classes = (MultiPartParser, FormParser)  # Resim yükleme desteği


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# 🚀 ID'ye göre Car Getir
class CarDetailView(APIView):
    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 🚀 Car Güncelleme
class CarUpdateView(APIView):
    def put(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🚀 Car Silme (Bağlı Resimleri de Sil)
class CarDeleteView(APIView):
    def delete(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        car.images.all().delete()  # Araca bağlı resimleri sil
        car.delete()  # Aracı sil
        return Response(
            {"message": "Car and its images deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
