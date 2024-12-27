

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from page.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("cars/", include("page.urls")),

    
    # API
    path("api/cars/", include("page.api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
