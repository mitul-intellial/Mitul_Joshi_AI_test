import requests

def get_weather_data(latitude, longitude):
    """
    Fetches weather data from the Open-Meteo API for the given latitude and longitude.

    Args:
        latitude (float): The latitude for which to fetch weather data.
        longitude (float): The longitude for which to fetch weather data.

    Returns:
        dict: A dictionary containing the weather data, or None if an error occurs.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def summarize_weather(data: dict) -> dict:
    """
    Extracts a summary of the weather from the raw data.

    Args:
        data: A dictionary containing the 'current_weather' data from the API.

    Returns:
        A dictionary with the summarized weather information.
    """
    current_weather = data.get("current_weather", {})
    return {
        "temperature": current_weather.get("temperature"),
        "windspeed": current_weather.get("windspeed"),
        "winddirection": current_weather.get("winddirection"),
        "time": current_weather.get("time"),
    }