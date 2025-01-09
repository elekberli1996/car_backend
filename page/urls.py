from django.urls import path
from .views import home, create_car

# cars/home/
# cars/create/

app_name = "core"
urlpatterns = [
    path("home/", home, name="home"),
    path("create/", create_car, name="create_car"),
]
