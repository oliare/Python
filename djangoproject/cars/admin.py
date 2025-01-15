from django.contrib import admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price']
    search_fields = ['brand', 'model']
    list_filter = ['brand', 'year']
    ordering = ['year']

admin.site.register(Car, CarAdmin)
