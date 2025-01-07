from django.contrib import admin
from .models import Car, CarImage

# Register your models here.


# CarImage modelini araba modeline eklemek için inline formu
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  # Başlangıçta bir boş form gösterilecek


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "price", "mileage", "created_at")
    list_filter = ("brand", "vehicle_type", "fuel_type",  "year", "price")
    search_fields = ("brand", "model", "year")
    ordering = ("-year", "-price")
    inlines = [CarImageInline]

    fieldsets = (
        ("General Information", {
            "fields": (("brand", "model"), ("year", "price"), ("mileage", "fuel_type")),
            "classes": ("wide",),
        }),
        ("Technical Specifications", {
            "fields": (("transmission", "color"), ("vehicle_type", "condition")),
            "classes": ("wide",),
        }),
        ("Engine Details", {
            "fields": (("horsepower", "engine_displacement"),),
            "classes": ("wide",),
        }),
        ("Description", {
            "fields": ("description",),
            "classes": ("collapse",),  # This section is collapsible.
        }),
    )

