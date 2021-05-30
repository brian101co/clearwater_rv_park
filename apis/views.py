import requests
import json

from django.shortcuts import render
from django.http import JsonResponse
from clearwater.settings import base

def get_current_weather(request):
    response = requests.get("https://api.weatherapi.com/v1/current.json",
        params={
            'key': base.WEATHER_API_KEY,
            'q': "39426",
        }
    )
    if response.status_code == 200:
        return JsonResponse(response.json())
    return JsonResponse({"error": "Missing API Key"}, status=500)
    