from fastapi import FastAPI
from app.core.aggregator import aggregate
from app.core.scorer import calculate_score
from app.models.schemas import AggregatedResponse

app = FastAPI()

@app.get("/travel-signal", response_model=AggregatedResponse)
async def travel_signal(
    destination: str,
    start_date: str,
    end_date: str,
    budget: float | None = None
):
    signals, missing = await aggregate(destination, budget)
    score = calculate_score(signals)

    explanation = {
        key: signal.dict()
        for key, signal in signals.items()
    }

    return AggregatedResponse(
        destination=destination,
        date_range=f"{start_date} to {end_date}",
        score=score,
        explanation=explanation,
        missing_signals=missing
    )


