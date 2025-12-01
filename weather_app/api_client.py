"""
API client for fetching weather data.
"""

import requests

def get_weather_data(lat: float, lon: float) -> dict:
    """
    Fetches weather data from the Open-Meteo API for the given latitude and longitude.

    Args:
        lat: Latitude.
        lon: Longitude.

    Returns:
        A dictionary containing the current weather data.

    Raises:
        ValueError: If the latitude or longitude are out of the valid range.
        requests.exceptions.RequestException: For network-related errors.
        requests.exceptions.HTTPError: For HTTP errors (e.g., 4xx, 5xx).
    """
    if not -90 <= lat <= 90:
        raise ValueError("Invalid latitude. Must be between -90 and 90.")
    if not -180 <= lon <= 180:
        raise ValueError("Invalid longitude. Must be between -180 and 180.")

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if "current_weather" not in data:
            raise ValueError("API response did not contain 'current_weather' data.")
        return data["current_weather"]
    except requests.exceptions.JSONDecodeError as e:
        raise ValueError("Failed to decode JSON response from API.") from e
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"API request failed: {e}") from e

if __name__ == "__main__":
    try:
        # Example: New York City
        latitude = 40.71
        longitude = -74.01
        weather = get_weather_data(latitude, longitude)
        print(f"Current weather in New York City: {weather}")
    except (ValueError, requests.exceptions.RequestException) as error:
        print(f"An error occurred: {error}")
