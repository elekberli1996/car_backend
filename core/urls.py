from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from page.views import home
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from account.api.auth.security import JWTAuthentication


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Mobil uygulama için REST API dokümantasyonu",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("cars/", include("page.urls")),
    #
    #
    # API
    path("api/cars/", include("page.api.urls")),
    path("api/auth/", include("account.api.urls")),
    #
    #
    # Swagger Dokümantasyonu
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    re_path(
        r"^api/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
