from app.utils.http import fetch_json
from app.models.schemas import SafetySignal
from app.utils.geocode import resolve_country_code

REGION_RISK = {
    "Europe": 0.3,
    "Asia": 0.4,
    "Americas": 0.4,
    "Africa": 0.6,
    "Oceania": 0.2
}

async def get_safety(destination: str) -> SafetySignal:
    try:
        country_code = await resolve_country_code(destination)

        if not country_code:
            return SafetySignal(advisory_level=None, risk=0.5)

        url = f"https://restcountries.com/v3.1/alpha/{country_code}"
        data = await fetch_json(url)

        if not data or not isinstance(data, list):
            return SafetySignal(advisory_level=None, risk=0.5)

        country = data[0]
        region = country.get("region")

        risk = REGION_RISK.get(region, 0.5)

        return SafetySignal(
            advisory_level=region,
            risk=risk
        )

    except Exception:
        return SafetySignal(advisory_level=None, risk=0.5)
