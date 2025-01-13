import os
from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms.create import CreateCar
from cars.forms.edit import EditCar
from django.conf import settings

def list(request):
    cars = Car.objects.all()
    return render(request, "list.html", {"cars": cars})

def catalog(request):
    cars = Car.objects.all()
    return render(request, "catalog.html", {"cars": cars})

def create(request):
    form = CreateCar()

    if request.method == "POST":
        form = CreateCar(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "create.html", {"form": form, "return_url": "/"})


def edit(request, id):
    try: car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")

    form = EditCar(instance=car)
    if request.method == "POST":
        form = CreateCar(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect("/cars")

    return render(request, "edit.html", {"form": form, "return_url": "/"})

def details(request, id):
    try: car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")
    return render(request, "details.html", {"car": car, "return_url": "/"})


def delete(request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")
    
    if car.photo:  
        path = os.path.join(settings.MEDIA_ROOT, car.photo.name)  # Use MEDIA_ROOT for file path
        if os.path.exists(path):
            os.remove(path)

    car.delete() 
    return redirect("/cars/")
