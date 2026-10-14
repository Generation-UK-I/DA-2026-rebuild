"""
Working with APIs and JSON: a first example
===========================================

Uses the Open-Meteo forecast API (no API key or signup needed).
Docs: https://open-meteo.com/en/docs

Setup:   pip install requests pandas
Run:     python weather_api_demo.py
"""

import json

import pandas as pd
import requests

# 1. The endpoint (the base URL) and the parameters (the "query string")
URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 51.752,           # Oxford, UK
    "longitude": -1.2577,
    "hourly": "temperature_2m,precipitation,wind_speed_10m",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Europe/London",
    "forecast_days": 7,
}


def fetch_weather(url: str, params: dict) -> dict:
    """Send a GET request and return the response body parsed as a dict."""
    response = requests.get(url, params=params, timeout=10)
    print("Request URL :", response.url)          # see exactly what was sent
    print("Status code :", response.status_code)  # 200 = OK
    response.raise_for_status()                   # raise an error on 4xx/5xx
    return response.json()                        # JSON text -> Python dict


def main():
    data = fetch_weather(URL, params)

    # 2. Explore the JSON structure
    print("\nTop-level keys:", list(data.keys()))
    print("\nFull JSON (first 800 characters):")
    print(json.dumps(data, indent=2)[:800], "...\n")

    # 3. Navigate nested JSON: dicts hold named values, lists hold sequences
    print("Timezone      :", data["timezone"])
    print("Daily units   :", data["daily_units"])
    print("First 3 days  :", data["daily"]["time"][:3])

    # 4. Convert to a DataFrame for analysis
    daily = pd.DataFrame(data["daily"])
    daily["time"] = pd.to_datetime(daily["time"])
    print("\nDaily forecast:")
    print(daily)

    hourly = pd.DataFrame(data["hourly"])
    hourly["time"] = pd.to_datetime(hourly["time"])
    print(f"\nHourly data: {hourly.shape[0]} rows x {hourly.shape[1]} columns")
    print(hourly.describe())

    # 5. A tiny bit of analysis
    hottest = daily.loc[daily["temperature_2m_max"].idxmax()]
    print(
        f"\nWarmest day: {hottest['time'].date()} "
        f"at {hottest['temperature_2m_max']} {data['daily_units']['temperature_2m_max']}"
    )

    # 6. Save the raw JSON so students can inspect it in an editor
    with open("weather_response.json", "w") as f:
        json.dump(data, f, indent=2)
    print("\nSaved raw response to weather_response.json")


if __name__ == "__main__":
    main()