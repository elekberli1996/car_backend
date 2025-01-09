from django.urls import path
from .views import home, create_car, show_detail

# cars/home/
# cars/create/

app_name = "core"
urlpatterns = [
    path("home/", home, name="home"),
    path("home/<int:id>", show_detail, name="detail"),
    path("create/", create_car, name="create_car"),
]
