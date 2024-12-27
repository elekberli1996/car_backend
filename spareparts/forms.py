from django import forms
from .models import Parts, PartImage


""" multiple file """
class MultipleFileInput(forms.ClearableFileInput):
        allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    """Django'nun varsayılan FileField'ını multiple file yüklemeyi destekleyecek hale getiriyoruz."""

    def __init__(self, *args, **kwargs):
        kwargs["widget"] = MultipleFileInput(attrs={"multiple": True})
        super().__init__(*args, **kwargs)


class PartForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = [
            "brand", "model",'part_name',"cond","price","currency",
            "information", "main_img", "name", "city", "tel"
        ] 