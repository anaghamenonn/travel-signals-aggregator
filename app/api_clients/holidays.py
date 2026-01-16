from app.utils.http import fetch_json
from app.models.schemas import HolidaySignal

async def get_holidays(country_code: str, year: int):
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    data = await fetch_json(url)

    has_holiday = bool(data)
    risk = 0.4 if has_holiday else 0.1

    return HolidaySignal(
        has_holiday=has_holiday,
        risk=risk
    )
