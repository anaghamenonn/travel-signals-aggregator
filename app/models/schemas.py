from pydantic import BaseModel
from typing import Optional, Union

class WeatherSignal(BaseModel):
    avg_temp: Optional[float]
    condition: Optional[str]
    risk: float

class HolidaySignal(BaseModel):
    has_holiday: bool
    risk: float

class CurrencySignal(BaseModel):
    rate: Optional[float]
    risk: float

class SafetySignal(BaseModel):
    advisory_level: Optional[Union[int, str]]
    risk: float

class FlightSignal(BaseModel):
    estimated_cost: Optional[float]
    risk: float

class AggregatedResponse(BaseModel):
    destination: str
    date_range: str
    score: float
    explanation: dict
    missing_signals: list
