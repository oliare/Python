from django import forms
from cars.models import Car


class CreateCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__" 
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
        }