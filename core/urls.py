

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from page.views import home
from page.views import home
from spareparts.views import parts,add_part,part_detail
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),

    path("parts/", parts, name="parts"),
    path("add_part/", add_part, name="add_part"),
    path("part_detail/<int:id>", part_detail, name="part_detail"),

    path("admin/", admin.site.urls),
    path("cars/", include("page.urls")),

    
    # API
    path("api/cars/", include("page.api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
