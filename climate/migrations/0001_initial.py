# Generated by Django 3.2.6 on 2021-09-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_info', models.CharField(max_length=200)),
                ('weather_loc', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
