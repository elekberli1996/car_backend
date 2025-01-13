from django.urls import path
from .views import parts, add_part, part_detail


urlpatterns = [
    path("parts/", parts, name="parts"),
    path("add/", add_part, name="add_part"),
    path("<int:id>/", part_detail, name="part_detail"),
]
