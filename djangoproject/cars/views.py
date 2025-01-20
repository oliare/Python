import os
from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms.create import CreateCar
from cars.forms.edit import EditCar
from django.conf import settings
from django.forms import model_to_dict
from django.contrib import messages


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
            messages.success(request, "Car created successfully!")  
            return redirect("/")
        else:
            messages.error(request, "Invalid data!")
    
    print(Car.CATEGORY_CHOICES)

    return render(request, "create.html", {"form": form, "return_url": "/", "category": Car.CATEGORY_CHOICES})


def edit(request, id):
    try: car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")

    form = EditCar(instance=car)
    if request.method == "POST":
        form = EditCar(request.POST, instance=car)

        if 'photo' in request.FILES: 
            if car.photo: 
                car.photo.delete()
            car.photo = request.FILES['photo']  

        if form.is_valid():
            form.save()
            messages.success(request, "Car details updated successfully!") 
            return redirect("/cars")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "edit.html", {"form": form, "return_url": "/"})

def details(request, id):
    try: car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")
    return render(request, "details.html", {
        "car": {
            **model_to_dict(car),
            "category": Car.CATEGORY_CHOICES[car.category][1]
        }, 
        "return_url": "/"})

def delete(request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")
    
    try:
        if car.photo:  
            path = os.path.join(settings.MEDIA_ROOT, car.photo.name)
            if os.path.exists(path):
                os.remove(path)

        car.delete() 
        messages.success(request, "Car deleted successfully!") 
    except Exception:
        messages.error(request, f"Error deleting car")

    return redirect("/cars/")
