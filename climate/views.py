from django.shortcuts import render
from django.http import HttpResponse
from pyowm import OWM
from pyowm.weatherapi25.weather import Weather
from .models import SaveWeather

def index(request):
    return HttpResponse("This is the weather site!")

def weather(request):
    API_key = '3bc15af9a0d73083998225ddcac9f79f'
    owm = OWM(API_key)
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place('Seoul,KR')      
    w = obs.weather
    # print(w)
    res = w.status 
    # print(res) # Rain
    res1 = w.detailed_status
    # print(res1) # moderate/light rain

    weather = SaveWeather(weather_info=res, weather_loc='Seoul,KR')
    weather.save()

    # location.save()

    w2 = obs.weather.wind()
    # print(w2) 
    return HttpResponse(weather)

# def location(request):
#     API_key = '3bc15af9a0d73083998225ddcac9f79f'
#     owm = OWM(API_key)
#     mgr = owm.weather_manager()
#     obs = mgr.weather_at_place('London,GB') 
#     return HttpResponse(obs)

# def savedweather(request):
#     asavedweather = SaveWeather
#     return HttpResponse(asavedweather)

