from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def make_url(city_name: str) -> str:
    """ convert url address """

    return f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid=${{secrets.WEATHER_API_KEY}}'


def make_context(data: dict, name: str) -> dict:
    """ get request and make context data """

    city_info = {
        'city': name,
        'temp': data["main"]["temp"],
        'feels_like': data["main"]["feels_like"],
        'pressure': data["main"]["pressure"],
        'icon': data["weather"][0]["icon"],
        'wind_speed': data["wind"]["speed"]
    }
    return city_info


def main(request):
    """ main function """

    if request.method == 'POST':

        form = CityForm(request.POST)
        try:
            form.save()
        except ValueError:
            pass

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        url = make_url(city.name)
        response = requests.get(url).json()
        data = make_context(response, city.name)
        all_cities.append(data)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


def delete(request, name):

    city = City.objects.get(name=name)
    try:
        city.delete()
        return HttpResponseRedirect("/")
    except city.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
