from django.shortcuts import render, redirect, get_object_or_404
from page.models import CarBrand
from .models import Parts, PartImage
from .forms import PartForm
from django.db import transaction


def parts(request):
    parts = Parts.objects.all()

    context = {"parts": parts}
    return render(request, "parts.html", context)


def add_part(request):

    brands = CarBrand.objects.all()

    if request.method == "POST":
        form = PartForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                with transaction.atomic():
                    part_instance = form.save()
                    part_images = request.FILES.getlist("car_images")

                    if part_images:
                        images_to_create = [
                            PartImage(part=part_instance, image=image)
                            for image in part_images
                        ]
                        PartImage.objects.bulk_create(images_to_create)

                return redirect("core:home")

            except Exception:
                form.add_error(None, "Xəta baş verdi. Zəhmət olmasa yenidən yoxlayın.")

    else:
        form = PartForm()

    return render(request, "add_part.html", {"form": form, "brands": brands})


#
