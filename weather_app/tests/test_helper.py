
import pytest
from unittest.mock import patch
import requests
from weather_app.helper import get_weather_data

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
