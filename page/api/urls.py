from django.urls import path
from .views import CarCreateView, BrandModelsAPIView, HomeAPIView


app_name = "api"  # API uygulaması için app_name

urlpatterns = [
    path("home/", HomeAPIView.as_view(), name="api_home"),
    path("add/", CarCreateView.as_view(), name="api_car_add"),
    # path("addform/", CarFormView.as_view(), name="api_model"),
    path(
        "brand/model/<str:brand_name>",
        BrandModelsAPIView.as_view(),
        name="brand-models",
    ),
]
