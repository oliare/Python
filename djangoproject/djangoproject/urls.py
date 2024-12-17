# from djangoproject.users import admin
from django.urls import path
from django.urls import include, path

from users import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.home),
    path("about/", views.about),
    path("users/", include("users.urls")),
]