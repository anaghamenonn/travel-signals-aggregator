import asyncio
import random
from datetime import datetime
from app.models.schemas import FlightSignal

async def get_flight_cost(destination: str, budget: float | None = None):
    await asyncio.sleep(random.uniform(0.5, 1.5))

    if random.random() < 0.1:
        return None

    base_price = random.randint(400, 700)

    demand_factor = random.choice([1.0, 1.2, 1.4])

    month = datetime.now().month
    if month in [6, 7, 8, 12]:
        season_factor = 1.3 
    else:
        season_factor = 1.0

    estimated_cost = int(base_price * demand_factor * season_factor)

    if budget is None:
        risk = 0.4
    else:
        ratio = estimated_cost / budget

        if ratio <= 0.6:
            risk = 0.2
        elif ratio <= 0.9:
            risk = 0.4
        elif ratio <= 1.1:
            risk = 0.6
        else:
            risk = 0.8

    return FlightSignal(
        estimated_cost=estimated_cost,
        risk=risk
    )
