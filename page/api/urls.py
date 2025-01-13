from django.urls import path
from .views import (
    CarCreateView,
    BrandModelsAPIView,
    CarDetailView,    
    home_view,
    CarFilterView,
    CarFilterBrandAPIView,
)


app_name = "api_page" 

urlpatterns = [
    path("home/", home_view, name="api_home"),
    path("add/", CarCreateView.as_view(), name="api_car_add"),
    path("<int:pk>/", CarDetailView.as_view(), name="api_car_detail"),
    path("filter/", CarFilterView.as_view(), name="api_car_filter"),
    path("filter/<str:brand>", CarFilterBrandAPIView.as_view(), name="api_filter_brand"),
    path("model/<str:brand_name>/", BrandModelsAPIView.as_view(), name="api_models"),
]
