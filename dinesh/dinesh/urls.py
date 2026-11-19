from django.contrib import admin
from django.urls import path
from areaapp import views


urlpatterns = [path('', views.calculate_rate, name='calculate_rate'),]