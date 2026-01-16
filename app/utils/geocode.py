from app.utils.http import fetch_json
from app.config import WEATHER_API_KEY

async def resolve_country_code(destination: str) -> str | None:
    if not WEATHER_API_KEY:
        return None

    url = (
        "https://api.openweathermap.org/geo/1.0/direct"
        f"?q={destination}&limit=1&appid={WEATHER_API_KEY}"
    )

    data = await fetch_json(url)

    if not data or len(data) == 0:
        return None

    return data[0].get("country")
