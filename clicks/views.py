from datetime import datetime
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Client
from .actions import seed_data
from config.mongo import totals_collection


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
    # Retreive all clients
    all_clients = list(Client.objects.all())
    # Sum up all the clicks
    total_clicks = sum(client.total_clicks for client in all_clients)
    # Calculate an average of clients' clicking speed
    average_clicking_speed = sum(
        client.average_clicking_speed for client in all_clients
    ) / len(all_clients)

    # Create a document or update an existing one
    retreived_document = totals_collection.find_one()
    if retreived_document is not None:
        update_operation = {
            "$set": {
                "total_clicks": total_clicks,
                "average_clicking_speed": average_clicking_speed,
            }
        }
        result = totals_collection.update_one({}, update_operation)
    else:
        retreived_document = totals_collection.insert_one(
            {
                "total_clicks": total_clicks,
                "average_clicking_speed": average_clicking_speed,
            }
        )

    # Define context either from the database document:
    retreived_document = totals_collection.find_one()
    if retreived_document is not None:
        context = {
            "total_clicks": retreived_document["total_clicks"],
            "average_clicking_speed": retreived_document["average_clicking_speed"],
        }
    # Or from the calculated variables
    else:
        context = {
            "total_clicks": total_clicks,
            "average_clicking_speed": average_clicking_speed,
        }

    # Render the template
    return render(request=request, template_name="clicks/totals.html", context=context)
