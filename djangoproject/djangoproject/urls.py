from django.urls import path
from django.urls import include, path

from users import views

urlpatterns = [
    path("", views.home),
    path("list/", views.list),
    path('details/<int:id>/', views.details), 
]

