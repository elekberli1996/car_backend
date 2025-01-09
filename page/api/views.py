from rest_framework import generics
from ..models import Car
from .serializers import CarSerializer
from django.views.generic import TemplateView
from ..models import CarBrand  # Örnek olarak marka bilgisini alıyoruz


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarFormView(TemplateView):
    template_name = "add_car.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["car_marka_opts"] = CarBrand.objects.all()

        context["other_data"] = "Some additional data"

        return context
