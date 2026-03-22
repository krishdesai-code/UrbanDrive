import math
from datetime import datetime

def calculate_flexible_rent(start_datetime, end_datetime, daily_rate, hourly_rate):
    if end_datetime <= start_datetime:
        raise ValueError("End datetime must be after start datetime")

    duration = end_datetime - start_datetime
    total_hours = duration.total_seconds() / 3600

    if total_hours >= 24:
        days = math.ceil(total_hours / 24)
        total_rent = days * daily_rate
    else:
        total_rent = total_hours * hourly_rate

    return round(total_rent, 2)