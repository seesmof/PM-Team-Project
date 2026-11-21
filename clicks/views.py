import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    context = {
        "name": "Oleh",
        "age": 21,
    }
    return JsonResponse(context)
