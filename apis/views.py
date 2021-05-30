import requests
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def get_current_weather(request):
    api_key = settings.API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?zip=39426&units=imperial&appid={api_key}"
    r = requests.get(url=url)
    return JsonResponse(r.json())
    