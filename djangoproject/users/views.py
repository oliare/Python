from django.http import HttpResponse
from django.shortcuts import render
from users.models import User

# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})

def list(request):
    users = User.objects.all()
    return render(request, "list.html", {"users": users})

def details(request, id):
    user = User.objects.get(pk=id)
    return render(request, "details.html", {"user": user})

def about(request):
    return HttpResponse("<h1>About Page!</h1>")
