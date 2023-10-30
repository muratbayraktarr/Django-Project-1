from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.conf.urls.static import static
import statistics


urlpatterns = [
    path('calendar/', views.calendar_request, name='calendar_request'),
    path('basicform/', views.basic_request, name='basic_request'),
    path('calculator/', views.calculator_request, name='calculator_request'),
    path('notekle/', views.not_ekle, name='not_ekle'),
]