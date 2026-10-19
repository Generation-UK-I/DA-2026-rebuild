"""
Working with APIs and JSON: a first example (no pandas)
=======================================================

Uses the Open-Meteo forecast API (no API key or signup needed).
Docs: https://open-meteo.com/en/docs

Setup:   pip install requests
Run:     python weather_api_demo_no_pandas.py
"""

import json

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

    # 4. Loop over parallel lists (same position = same day)
    daily = data["daily"]
    units = data["daily_units"]
    print("\nDaily forecast:")
    for i in range(len(daily["time"])):
        print(
            f"{daily['time'][i]}  "
            f"max {daily['temperature_2m_max'][i]}{units['temperature_2m_max']}  "
            f"min {daily['temperature_2m_min'][i]}{units['temperature_2m_min']}  "
            f"rain {daily['precipitation_sum'][i]}{units['precipitation_sum']}"
        )

    # 5. A tiny bit of analysis with built-in Python
    max_temps = daily["temperature_2m_max"]
    hottest_max = max(max_temps)
    hottest_index = max_temps.index(hottest_max)
    print(
        f"\nWarmest day: {daily['time'][hottest_index]} "
        f"at {hottest_max}{units['temperature_2m_max']}"
    )

    hourly_temps = data["hourly"]["temperature_2m"]
    print(f"\nHourly readings: {len(hourly_temps)}")
    print(f"Average hourly temperature: {sum(hourly_temps) / len(hourly_temps):.1f}")

    # 6. Save the raw JSON so students can inspect it in an editor
    with open("weather_response.json", "w") as f:
        json.dump(data, f, indent=2)
    print("\nSaved raw response to weather_response.json")


if __name__ == "__main__":
    main()
