from django.urls import path

from cars import views

urlpatterns = [
    path('', views.list),
    path('list/', views.list),
    path('details/<int:id>/', views.details), 
    path('delete/<int:id>/', views.delete), 
]
