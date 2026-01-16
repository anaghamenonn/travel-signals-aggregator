import asyncio
from app.api_clients.weather import get_weather
from app.api_clients.holidays import get_holidays
from app.api_clients.currency import get_currency_rate
from app.api_clients.safety import get_safety
from app.api_clients.flights import get_flight_cost

async def aggregate(destination: str, budget: float | None = None):
    tasks = {
        "weather": get_weather(destination),
        "holidays": get_holidays("FR", 2026),
        "currency": get_currency_rate(),
        "safety": get_safety(destination),
        "flights": get_flight_cost(destination, budget)
    }

    results = {}
    missing = []

    responses = await asyncio.gather(*tasks.values(), return_exceptions=True)

    for key, response in zip(tasks.keys(), responses):
        if isinstance(response, Exception) or response is None:
            missing.append(key)
        else:
            results[key] = response

    return results, missing



