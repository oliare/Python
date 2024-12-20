from django import forms
from cars.models import Car


class CreateCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__" 