from datetime import datetime
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Client
from .actions import seed_data


def index(request: HttpRequest) -> HttpResponse:
    # Render the template.
    return render(request=request, template_name="clicks/index.html", context={})


def status(request: HttpRequest) -> HttpResponse:
    # Fill in the database with 3 random objects unless already created
    seed_data()
    # Define context and add the mock data to it.
    context = {"users": Client.objects.all()}

    # Render the template.
    return render(request=request, template_name="clicks/status.html", context=context)


def totals(requets: HttpRequest):
    return JsonResponse({})
