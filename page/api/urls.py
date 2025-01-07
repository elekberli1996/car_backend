from django.urls import path

# from . import views
from .views import *


urlpatterns = [
    path("", CarListView.as_view(), name="car-list"),
    path("create/", CarCreateView.as_view(), name="car-create"),
    path("<int:car_id>/", CarDetailView.as_view(), name="car-detail"),
    path("<int:car_id>/update/", CarUpdateView.as_view(), name="car-update"),
    path("<int:car_id>/delete/", CarDeleteView.as_view(), name="car-delete"),
]
