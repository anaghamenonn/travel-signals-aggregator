# Travel Signals Aggregator

## Overview
The Travel Signals Aggregator provides a structured and explainable assessment
of travel feasibility for a given destination and date range.

It aggregates multiple third-party travel-related signals such as:
- Weather conditions
- Public holidays
- Currency exchange rates
- Safety context
- Flight cost estimates

The goal is to help users quickly evaluate risk and readiness before
committing time or money to a trip.

---

## Architecture

### Backend (FastAPI)
- API adapters for each external provider
- Asynchronous aggregation using `asyncio`
- Unified internal data schema
- Graceful degradation when APIs fail

### Frontend (React.js)
- Functional components with hooks
- API-first design
- Environment-based backend configuration
- Clear visualization of signals and risks

The frontend is intentionally minimal and exists to demonstrate how the
backend output can be consumed and explained.

---

## Third-Party Integrations

| Signal | Provider | Type |
|------|--------|------|
| Weather | OpenWeatherMap | Real |
| Public Holidays | Nager.Date | Real |
| Currency | Frankfurter | Real |
| Safety | RestCountries (region heuristic) | Real (Derived) |
| Flight Cost | Simulated | Mocked |

Mocked APIs simulate realistic latency, variability, and failure scenarios
where real-world APIs are impractical or restricted.

---

## API Usage

### Endpoint
GET /travel-signal


### Query Parameters
- `destination` (string, required)
- `start_date` (string, required)
- `end_date` (string, required)
- `budget` (number, optional)

### Example (Postman / Browser)
Use the following URL to test directly:  
http://localhost:8000/travel-signal?destination=Paris&start_date=2026-03-10&end_date=2026-03-15&budget=5000

## Running the Project

### Backend Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Environment variables (create .env in root):
WEATHER_API_KEY=<your_openweather_api_key>
```

### Frontend Setup
```
cd frontend
npm install
npm start
Environment variables (create frontend/.env):
REACT_APP_API_URL=http://localhost:8000
```
