from django.db import models


class SaveWeather(models.Model):
    weather_info = models.CharField(max_length=200)
    weather_loc = models.CharField(max_length=200, null=True)
    # pub_date = models.DateTimeField('date published')
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class WeatherLocation(models.Model):
#     weather_loc = models.CharField(max_length=200)
#     def __str__(self):
#         return self.weather_loc