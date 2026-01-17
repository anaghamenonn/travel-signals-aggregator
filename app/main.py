from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.aggregator import aggregate
from app.core.scorer import calculate_score
from app.models.schemas import AggregatedResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://travel-signals-aggregator.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Travel Signals Aggregator API is running",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

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


