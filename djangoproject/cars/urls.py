from django.urls import path

from cars import views

urlpatterns = [
    path('', views.list),
    path('create/', views.create),
    path('catalog/', views.catalog),
    path('edit/<int:id>/', views.edit),
    path('details/<int:id>/', views.details), 
    path('delete/<int:id>/', views.delete), 
]
