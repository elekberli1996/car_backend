from django import forms
from .models import Car, CarImage


class MultipleFileInput(forms.ClearableFileInput):
    """Django'da multiple file input için özel widget."""

    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    """Django'nun varsayılan FileField'ını multiple file yüklemeyi destekleyecek hale getiriyoruz."""

    def __init__(self, *args, **kwargs):
        kwargs["widget"] = MultipleFileInput(attrs={"multiple": True})
        super().__init__(*args, **kwargs)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "brand", "model", "vehicle_type", "color", "fuel_type", "transmission",
            "mileage", "unit", "year", "engine_size", "power", "vin","price",
            "currency", "information", "main_img", "name", "city", "tel"
        ] 