from app.utils.http import fetch_json
from app.models.schemas import CurrencySignal

async def get_currency_rate(base="USD", target="EUR"):
    url = f"https://api.frankfurter.app/latest?from={base}&to={target}"
    data = await fetch_json(url)

    if not data:
        return CurrencySignal(rate=None, risk=0.3)

    rate = data["rates"][target]
    risk = 0.2 if rate < 1.2 else 0.4

    return CurrencySignal(rate=rate, risk=risk)
