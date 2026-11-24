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


def totals(request: HttpRequest):
    all_clients = list(Client.objects.all())
    total_clicks = sum(client.total_clicks for client in all_clients)
    average_clicking_speed = sum(
        client.average_clicking_speed for client in all_clients
    ) / len(all_clients)

    context = {
        "total_clicks": total_clicks,
        "average_clicking_speed": average_clicking_speed,
    }
    return render(request=request, template_name="clicks/totals.html", context=context)
