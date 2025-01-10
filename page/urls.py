from django.urls import path
from .views import home, add_car, car_detail

# cars/home/
# cars/add/
# cars/1/

app_name = "core"
urlpatterns = [
    path("home/", home, name="home"),
    path("<int:id>/", car_detail, name="car_detail"),
    path("add/", add_car, name="add_car"),
]
