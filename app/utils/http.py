import httpx
import asyncio
from app.config import REQUEST_TIMEOUT, MAX_RETRIES

async def fetch_json(url: str, headers=None):
    headers = headers or {}

    for attempt in range(MAX_RETRIES + 1):
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                return response.json()
        except Exception:
            if attempt == MAX_RETRIES:
                return None
            await asyncio.sleep(0.5)

