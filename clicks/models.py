from datetime import datetime
from enum import StrEnum

from django.db import models
from dataclasses import dataclass


class StressLevel(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"


@dataclass
class Client:
    id: int | None
    name: str
    stress_level: StressLevel = StressLevel.low
    total_clicks: int = 0
    average_clicking_speed: float = 0.0
    last_activity: datetime | None = None
