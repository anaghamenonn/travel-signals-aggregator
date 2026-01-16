from app.utils.http import fetch_json
from app.models.schemas import WeatherSignal
from app.config import WEATHER_API_KEY

async def get_weather(destination: str):
    if not WEATHER_API_KEY:
        return WeatherSignal(
            avg_temp=None,
            condition=None,
            risk=0.5
        )

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={destination}&units=metric&appid={WEATHER_API_KEY}"
    )

    data = await fetch_json(url)

    if not data or "main" not in data:
        return WeatherSignal(
            avg_temp=None,
            condition=None,
            risk=0.5
        )

    temp = data["main"]["temp"]
    condition = data["weather"][0]["main"]

    if temp < 0 or temp > 40:
        risk = 0.7
    elif temp < 10:
        risk = 0.4
    else:
        risk = 0.2

    return WeatherSignal(
        avg_temp=temp,
        condition=condition,
        risk=risk
    )
