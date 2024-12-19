from django.shortcuts import redirect, render
from cars.models import Car

def list(request):
    cars = Car.objects.all()
    return render(request, "list.html", {"cars": cars})

def details(request, id):
    try: car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")
    return render(request, "details.html", {"car": car})

def delete(request, id):
    try: car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return render(request, "error_404.html")
    car.delete()
    return redirect("/cars/list") 
