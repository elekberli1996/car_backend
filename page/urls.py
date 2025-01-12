from django.urls import path
from .views import home, add_car, car_detail

# 
# cars/add/
# cars/1/

app_name = "page"
urlpatterns = [
    path("add/", add_car, name="add_car"),
    path("<int:id>/", car_detail, name="car_detail"),
]
