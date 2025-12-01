import pytest
from unittest.mock import patch
import requests
from weather_app.helper import get_weather_data, summarize_weather

@patch('weather_app.helper.requests.get')
def test_get_weather_data_success(mock_get):
    """
    Tests the get_weather_data function for a successful API call.
    """
    mock_response = {
        "latitude": 52.52,
        "longitude": 13.41,
        "current_weather": {
            "temperature": 20.0,
            "windspeed": 10.0,
            "weathercode": 3
        }
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    latitude = 52.52
    longitude = 13.41
    weather_data = get_weather_data(latitude, longitude)

    assert weather_data == mock_response

@patch('weather_app.helper.requests.get')
def test_get_weather_data_failure(mock_get):
    """
    Tests the get_weather_data function for a failed API call.
    """
    mock_get.side_effect = requests.exceptions.RequestException("Test error")

    latitude = 52.52
    longitude = 13.41
    weather_data = get_weather_data(latitude, longitude)

    assert weather_data is None

def test_summarize_weather_valid_data():
    """
    Test summarize_weather with a valid, complete data structure.
    """
    # Arrange
    raw_data = {
        "current_weather": {
            "temperature": 15.0,
            "windspeed": 5.5,
            "winddirection": 270,
            "time": "2025-12-01T14:00"
        }
    }
    expected_summary = {
        "temperature": 15.0,
        "windspeed": 5.5,
        "winddirection": 270,
        "time": "2025-12-01T14:00"
    }

    # Act
    summary = summarize_weather(raw_data)

    # Assert
    assert summary == expected_summary

def test_summarize_weather_missing_fields():
    """
    Test summarize_weather when some fields are missing from current_weather.
    """
    # Arrange
    raw_data = {
        "current_weather": {
            "temperature": 15.0,
            "time": "2025-12-01T14:00"
        }
    }
    expected_summary = {
        "temperature": 15.0,
        "windspeed": None,
        "winddirection": None,
        "time": "2025-12-01T14:00"
    }

    # Act
    summary = summarize_weather(raw_data)

    # Assert
    assert summary == expected_summary

def test_summarize_weather_missing_current_weather():
    """
    Test summarize_weather when the 'current_weather' key itself is missing.
    """
    # Arrange
    raw_data = {"latitude": 52.52}
    expected_summary = {
        "temperature": None,
        "windspeed": None,
        "winddirection": None,
        "time": None
    }

    # Act
    summary = summarize_weather(raw_data)

    # Assert
    assert summary == expected_summary