from datetime import datetime

from .models import Client


def seed_data():
    one = Client.objects.filter(full_name="Virginia Perry")
    if not one:
        one = Client(
            full_name="Virginia Perry",
            total_clicks=971,
            average_clicking_speed=16.4,
            last_activity=datetime.now(),
        )
        one.save()

    two = Client.objects.filter(full_name="Kenneth Fernandez")
    if not two:
        two = Client(
            full_name="Kenneth Fernandez",
            total_clicks=313,
            average_clicking_speed=14.0,
            last_activity=datetime.now(),
        )
        two.save()

    three = Client.objects.filter(full_name="Mattie Newton")
    if not three:
        three = Client(
            full_name="Mattie Newton",
            total_clicks=922,
            average_clicking_speed=95.3,
            last_activity=datetime.now(),
        )
        three.save()
