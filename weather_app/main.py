
import json
from weather_app.helper import get_weather_data

def validate_weather_data(data):
    """
    Validates the weather data to ensure it contains the required fields.

    Args:
        data (dict): The weather data to validate.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    if not data:
        return False

    required_fields = ["latitude", "longitude", "current_weather"]
    if not all(field in data for field in required_fields):
        return False

    current_weather = data.get("current_weather", {})
    required_weather_fields = ["temperature", "windspeed", "weathercode"]
    if not all(field in current_weather for field in required_weather_fields):
        return False

    return True

def main():
    """
    Main function to fetch, validate, and save weather data.
    """
    latitude = 52.52  # Example latitude (Berlin)
    longitude = 13.41  # Example longitude (Berlin)

    weather_data = get_weather_data(latitude, longitude)

    if validate_weather_data(weather_data):
        summary = {
            "latitude": weather_data["latitude"],
            "longitude": weather_data["longitude"],
            "temperature": weather_data["current_weather"]["temperature"],
            "windspeed": weather_data["current_weather"]["windspeed"],
            "weathercode": weather_data["current_weather"]["weathercode"]
        }

        try:
            with open("weather_summary.json", "w") as f:
                json.dump(summary, f, indent=4)
            print("Weather data saved to weather_summary.json")
        except IOError as e:
            print(f"Error saving weather data: {e}")
    else:
        print("Failed to fetch or validate weather data.")

if __name__ == "__main__":
    main()
