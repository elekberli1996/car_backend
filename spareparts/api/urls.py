from django.urls import path
from .views import PartCreateView


urlpatterns = [
    path("add/", PartCreateView.as_view(), name="api_part_add"),
]
