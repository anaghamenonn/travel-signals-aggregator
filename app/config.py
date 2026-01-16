import os
from dotenv import load_dotenv

load_dotenv()  

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
SAFETY_API_KEY = os.getenv("SAFETY_API_KEY")

print("WEATHER_API_KEY loaded:", bool(WEATHER_API_KEY))
print("SAFETY_API_KEY loaded:", bool(SAFETY_API_KEY))


REQUEST_TIMEOUT = 5
MAX_RETRIES = 2
