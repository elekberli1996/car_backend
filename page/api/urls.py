from django.urls import path
from .views import CarCreateView, CarFormView

urlpatterns = [
   path('create/', CarFormView.as_view(), name='car-form'),           # Formu göstermek için
    path('create-api/', CarCreateView.as_view(), name='car-create'),  # API'yi çağıran URL
]
