from django import forms
from cars.models import Car


class EditCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"  # all model fields  