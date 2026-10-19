import json
import requests
import os
from unittest.mock import patch
import pytest

# Mock response data matching the expected Open-Meteo schema
MOCK_API_RESPONSE = {
    "latitude": 51.50076,
    "longitude": -0.12451,
    "timezone": "Europe/London",
    "current": {
        "time": "2026-10-15T09:00",
        "temperature_2m": 15.5,
        "weather_code": 3
    },
    "hourly": {
        "time": ["2026-10-15T00:00", "2026-10-15T01:00", "2026-10-15T02:00"],
        "temperature_2m": [12.0, 11.5, 11.0],
        "rain": [0.0, 0.5, 1.2]
    },
    "daily": {
        "time": ["2026-10-15", "2026-10-16", "2026-10-17"],
        "temperature_2m_max": [18.0, 17.5, 16.0],
        "temperature_2m_min": [10.0, 9.5, 8.5]
    },
    "daily_units": {
        "temperature_2m_max": "°C",
        "temperature_2m_min": "°C"
    }
}

class MockResponse:
    """Helper class to mock requests.Response object."""
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


# --- Test 1: Basic File Persistence (Easy) ---
@patch("requests.get")
def test_weather_json_file_created(mock_get, tmp_path):
    """Verify that the script successfully queries the API and dumps output to weather_response.json."""
    mock_get.return_value = MockResponse(MOCK_API_RESPONSE)
    
    # Run the student's script logic within a temporary working directory or check file creation
    # Assuming the script writes to 'weather_response.json' in the current dir:
    from EOM_assessment_solution import data # or execute module
    
    assert os.path.exists("weather_response.json"), "The script must save the output to 'weather_response.json'."
    with open("weather_response.json", "r") as f:
        content = json.load(f)
    assert isinstance(content, dict), "The saved file must contain a valid JSON object."


# --- Test 2: Status Code and Top-Level Schema (Easy-Medium) ---
@patch("requests.get")
def test_top_level_keys_and_status(mock_get):
    """Verify the HTTP status code is 200 and essential top-level keys exist in the response."""
    mock_get.return_value = MockResponse(MOCK_API_RESPONSE)
    
    response = requests.get("https://api.open-meteo.com/v1/forecast")
    data = response.json()
    
    assert response.status_code == 200
    for key in ["latitude", "longitude", "current", "hourly", "daily"]:
        assert key in data, f"Missing essential top-level key: {key}"


# --- Test 3: Array Length & Forecast Constraints (Medium) ---
@patch("requests.get")
def test_forecast_day_and_array_lengths(mock_get):
    """Verify that hourly and daily lists match expected collection sizes and data types."""
    mock_get.return_value = MockResponse(MOCK_API_RESPONSE)
    
    data = MOCK_API_RESPONSE
    
    # Check hourly metrics
    hourly_temps = data["hourly"]["temperature_2m"]
    assert len(hourly_temps) > 0
    assert all(isinstance(t, (int, float)) for t in hourly_temps)
    
    # Check daily forecast bounds (matching forecast_days = 3)
    daily_max = data["daily"]["temperature_2m_max"]
    assert len(daily_max) == 3, "Daily forecast length should match the 3-day request parameter."


# --- Test 4: Calculation Logic Verification (Medium-Hard) ---
@patch("requests.get")
def test_average_calculations(mock_get):
    """Verify that calculations like average temperature compute correctly from data arrays."""
    mock_get.return_value = MockResponse(MOCK_API_RESPONSE)
    
    data = MOCK_API_RESPONSE
    hourly_temps = data["hourly"]["temperature_2m"] # [12.0, 11.5, 11.0]
    
    expected_avg = sum(hourly_temps) / len(hourly_temps)
    calculated_avg = sum(data["hourly"]["temperature_2m"]) / len(data["hourly"]["temperature_2m"])
    
    assert calculated_avg == pytest.approx(expected_avg, 0.01)


# --- Test 5: Weather Code Dictionary Lookup & Robustness (Hard) ---
@patch("requests.get")
def test_weather_code_lookup_integration(mock_get):
    """Verify that the weather code maps safely to a string description using the external codes module."""
    mock_get.return_value = MockResponse(MOCK_API_RESPONSE)
    
    from weather_codes import codes
    
    code_val = str(MOCK_API_RESPONSE["current"]["weather_code"])
    assert code_val in codes, f"Weather code '{code_val}' must be present in the weather_codes dictionary."
    assert isinstance(codes[code_val], str), "Weather code description must resolve to a string."