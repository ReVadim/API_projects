from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    """ get city name """

    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}
