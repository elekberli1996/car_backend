from django.contrib import admin
from .models import Car, CarImage, CarBrand, CarModel


# CarImage modelini Car modeline eklemek için inline formu
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  # Başlangıçta bir boş form gösterilecek


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "price", "mileage", "created_at")
    list_filter = (
        "brand",
        "vehicle_type",
        "fuel_type",
        "year",
        "price",
        "transmission",
        "city",
    )
    search_fields = ("brand", "model", "year", "vin", "city")
    ordering = ("-year", "-price")
    inlines = [CarImageInline]

    fieldsets = (
        (
            "General Information",
            {
                "fields": (
                    ("brand", "model"),
                    ("year", "price"),
                    ("mileage", "fuel_type"),
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Technical Specifications",
            {
                "fields": (("transmission", "color"), ("vehicle_type",)),
                "classes": ("wide",),
            },
        ),
        (
            "Owner & Location",
            {
                "fields": (("name", "tel"), "city"),
                "classes": ("wide",),
            },
        ),
        (
            "Images",
            {
                "fields": ("main_img",),
            },
        ),
        (
            "Additional Details",
            {
                "fields": ("information",),
                "classes": ("collapse",),
            },
        ),
    )


# Register CarBrand model
@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Display the brand name in the list view
    search_fields = ("name",)  # Allow searching by brand name


# Register CarModel model
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")  # Display model name and associated brand
    list_filter = ("brand",)  # Filter models by brand
    search_fields = ("name",)  # Allow searching by model name
