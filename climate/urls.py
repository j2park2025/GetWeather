from django.urls import path
from . import views
from . import models
# from django.urls import include, path

urlpatterns = [
    path('main', views.index, name='index'),
    path('weather', views.weather, name='weather'),
    # path('location', views.location, name='loc'),
    # path('savedweather', views.savedweather, name='sawe'),
    # path('climate/', include('climate.urls')),
]
