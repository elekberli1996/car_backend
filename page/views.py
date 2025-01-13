from django.shortcuts import render, redirect, get_object_or_404

from .models import Car, CarImage, CarBrand, CarModel
from .forms import CarForm
from django.db import transaction


def home(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, "home.html", context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    images = car.images.all()
    first_three_images = images[:3]
    remaining_images = images[3:]
    last_five_items = images[1:5]

    context = {
        "car": car,
        "images": "images",
        "first_three_images": first_three_images,
        "remaining_images": remaining_images,
    }
    return render(request, "car_detail.html", context)


def add_car(request):
    brands = CarBrand.objects.all()

    # if request.method == "POST":
    #     form = CarForm(request.POST, request.FILES)
    #     # print("POST data:", request.POST)
    #     # print("FILES data:", request.FILES)
    #     if form.is_valid():
    #         car_instance = form.save()
    #         car_images = request.FILES.getlist("car_images")
    #         for image in car_images:
    #             CarImage.objects.create(car=car_instance, image=image)
    #         return redirect("core:home")
    #     else:
    #         print("Form errors:", form.errors)
    # else:
    #     form = CarForm()
    # return render(request, "add_car.html", {"form": form, "brands": brands})
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                with transaction.atomic():
                    car_instance = form.save()
                    car_images = request.FILES.getlist("car_images")

                    if car_images:
                        images_to_create = [
                            CarImage(car=car_instance, image=image)
                            for image in car_images
                        ]
                        CarImage.objects.bulk_create(images_to_create)

                return redirect("core:home")

            except Exception:
                form.add_error(None, "Xəta baş verdi. Zəhmət olmasa yenidən yoxlayın.")

    else:
        form = CarForm()

    return render(request, "add_car.html", {"form": form, "brands": brands})
