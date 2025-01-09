from django.urls import path
from .views import CarCreateView, CarFormView, BrandModelsAPIView, HomeAPIView


app_name = "api"  # API uygulaması için app_name

urlpatterns = [
    path("home/", HomeAPIView.as_view(), name="api_home"),
    path("create/", CarFormView.as_view(), name="car-form"),
    path("create-api/", CarCreateView.as_view(), name="car-create"),
    path(
        "brands/<str:brand_name>/models/",
        BrandModelsAPIView.as_view(),
        name="brand-models",
    ),
]
