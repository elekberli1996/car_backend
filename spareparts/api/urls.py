from django.urls import path
from .views import PartCreateView, parts_home_view, PartDetailView


urlpatterns = [
    path("", parts_home_view, name="api_part_home"),
    path("add/", PartCreateView.as_view(), name="api_part_add"),
    path("<int:pk>/", PartDetailView.as_view(), name="api_part_detail"),
]
