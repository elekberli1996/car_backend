from django.urls import path
from .views import parts, add_part

#
# cars/add/
# cars/1/
# app_name = "spareparts"
urlpatterns = [
    path("parts/", parts, name="parts"),
    path("add/", add_part, name="add_part"),
]
