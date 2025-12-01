"""
Tests for the API client.
"""

import pytest
import requests
from unittest.mock import patch, Mock
from weather_app.api_client import get_weather_data

@patch('weather_app.api_client.requests.get')
def test_get_weather_data_success(mock_get):
    """
    Test successful API call to get_weather_data.
    """
    # Arrange
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "latitude": 40.71,
        "longitude": -74.01,
        "current_weather": {
            "temperature": 15.0,
            "windspeed": 5.0,
            "winddirection": 270,
            "time": "2025-12-01T12:00"
        }
    }
    mock_get.return_value = mock_response

    # Act
    lat, lon = 40.71, -74.01
    result = get_weather_data(lat, lon)

    # Assert
    mock_get.assert_called_once_with(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true",
        timeout=10
    )
    mock_response.raise_for_status.assert_called_once()
    assert result == mock_response.json.return_value["current_weather"]

@patch('weather_app.api_client.requests.get')
def test_get_weather_data_http_error(mock_get):
    """
    Test that get_weather_data raises RequestException on an HTTP error.
    """
    # Arrange
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
    mock_get.return_value = mock_response

    # Act & Assert
    with pytest.raises(requests.exceptions.RequestException):
        get_weather_data(40.71, -74.01)

def test_get_weather_data_invalid_coordinates():
    """
    Test that get_weather_data raises ValueError for invalid coordinates.
    """
    with pytest.raises(ValueError, match="Invalid latitude"):
        get_weather_data(91, 0)
    
    with pytest.raises(ValueError, match="Invalid longitude"):
        get_weather_data(0, 181)