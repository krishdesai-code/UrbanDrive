import math
from decimal import Decimal

def calculate_flexible_rent(start_datetime, end_datetime, daily_rate, hourly_rate):
    if end_datetime <= start_datetime:
        raise ValueError("End datetime must be after start datetime")

    duration = end_datetime - start_datetime
    total_hours = Decimal(str(duration.total_seconds() / 3600)) 

    hourly_rate = Decimal(hourly_rate)
    daily_rate = Decimal(daily_rate)

    if total_hours >= 24:
        days = (total_hours / Decimal("24")).quantize(Decimal("1"), rounding="ROUND_UP")
        total_rent = days * daily_rate
    else:
        total_rent = total_hours * hourly_rate

    return total_rent.quantize(Decimal("0.01"))