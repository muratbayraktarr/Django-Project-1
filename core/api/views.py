import os
from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.middleware import SessionMiddleware
from datetime import datetime, timedelta
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def calendar_request(request):
    return render(request, 'calendar.html')

def basic_request(request):
    context = dict()
    context['nots'] = Not.objects.all()
    return render(request, 'form.html', context)

def calculator_request(request):
    return render(request, 'calculator.html')


def not_ekle(request):
     if request.method == 'POST':
        field1 = request.POST['not']

        Not.objects.create(
            icerik = field1
        )
        return redirect('basic_request')
