from weather_codes import codes
import requests
import json

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 51.50076,
    "longitude": -0.12451,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
	"hourly": ["temperature_2m", "rain"],
	"current": ["temperature_2m", "weather_code"],
	"timezone": "Europe/London",
	"forecast_days": 3,
	"wind_speed_unit": "mph",
}

response = requests.get(url, params=params)
data = response.json()

print("Status code :", response.status_code)
# print("\nTop-level keys:", list(data.keys()))

hourly_temps = data["hourly"]["temperature_2m"]
print(f"\nHourly readings: {len(hourly_temps)}")
print(f"Average hourly temperature: {sum(hourly_temps) / len(hourly_temps):.1f}")

hourly_rain = data["hourly"]["rain"]
print(f"\nHourly readings: {len(hourly_rain)}")
print(f"Average hourly rain: {sum(hourly_rain) / len(hourly_rain):.1f}")

daily = data["daily"]
units = data["daily_units"]
print("\nDaily forecast:")
for i in range(len(daily["time"])):
    print(
        f"{daily['time'][i]}  "
        f"max {daily['temperature_2m_max'][i]}{units['temperature_2m_max']}  "
        f"min {daily['temperature_2m_min'][i]}{units['temperature_2m_min']}  "
    )

description = data['current']['weather_code']
text_desc = str(description)
print(codes[text_desc])

print(f"Current Temperature: {data['current']['temperature_2m']}C")

# print(f"\n\nFull json:\n{data}")

with open("weather_response.json", "w") as f:
    json.dump(data, f, indent=2)
print("\nSaved raw response to weather_response.json")

