from datetime import datetime
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from clicks.models import Client, StressLevel


def status(request: HttpRequest) -> HttpResponse:
    # Declare mock data with three users of randomly generated data.
    users_test_data: list[Client] = [
        Client(
            id=1,
            name="Alma Banks",
            stress_level=StressLevel.low,
            total_clicks=515,
            average_clicking_speed=4.3,
            last_activity=datetime.now(),
        ),
        Client(
            id=1,
            name="Noah Carter",
            stress_level=StressLevel.medium,
            total_clicks=387,
            average_clicking_speed=70.6,
            last_activity=datetime.now(),
        ),
        Client(
            id=1,
            name="Danny Wright",
            stress_level=StressLevel.high,
            total_clicks=779,
            average_clicking_speed=68.8,
            last_activity=datetime.now(),
        ),
    ]
    # Define context and add the mock data to it.
    context = {
        "users": users_test_data,
    }

    return render(request=request, template_name="clicks/status.html", context=context)
