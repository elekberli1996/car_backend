from django.shortcuts import render, redirect
from .models import Car, CarImage, CarBrand, CarModel
from .forms import CarForm


def home(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, "home.html", context)


def show_detail(request, id):
    print("id", id)
    return render(request, "add_car.html")


def create_car(request):
    brands = CarBrand.objects.all()

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)

        if form.is_valid():
            car_instance = form.save()
            car_images = request.FILES.getlist("car_images")
            for image in car_images:
                CarImage.objects.create(car=car_instance, image=image)

            return redirect("core:home")
        else:
            print("Form errors:", form.errors)

    else:
        form = CarForm()

    return render(request, "add_car.html", {"form": form, "brands": brands})
