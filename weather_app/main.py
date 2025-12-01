"""
Main application file for the weather app.
"""

import json
import sys
import os
import requests

# Adjust the path to import from parent directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api_client import get_weather_data
from helper import summarize_weather

# Hardcoded city coordinates
CITY_COORDINATES = {
    "new york": {"lat": 40.71, "lon": -74.01},
    "london": {"lat": 51.51, "lon": -0.13},
    "tokyo": {"lat": 35.68, "lon": 139.69},
    "sydney": {"lat": -33.87, "lon": 151.21},
    "paris": {"lat": 48.85, "lon": 2.35},
}

def main():
    """
    Main function to run the weather application.
    """
    # 1. Read city from user input
    city_name = input("Enter a city name: ").lower()

    # 2. Find coordinates
    if city_name not in CITY_COORDINATES:
        print(f"Error: City '{city_name}' not found. Please choose from: {', '.join(CITY_COORDINATES.keys())}")
        return

    coords = CITY_COORDINATES[city_name]
    lat, lon = coords["lat"], coords["lon"]
    print(f"Fetching weather for {city_name.title()} (Lat: {lat}, Lon: {lon})...")

    try:
        # 3. Call API
        raw_weather_data = get_weather_data(lat, lon)

        # The helper function expects the full API response structure
        # Let's wrap our data to match what summarize_weather expects
        api_response_mock = {"current_weather": raw_weather_data}
        
        # 4. Get summary
        weather_summary = summarize_weather(api_response_mock)

        # Print summary
        print("\n--- Weather Summary ---")
        for key, value in weather_summary.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        print("-----------------------")

        # 5. Save summary to JSON file
        # The JSON file is in the parent directory
        output_path = os.path.join(os.path.dirname(__file__), '..', 'weather_summary.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(weather_summary, f, indent=4)
        
        print(f"\nSummary saved to {os.path.abspath(output_path)}")

    except (ValueError, requests.exceptions.RequestException) as e:
        print(f"\nAn error occurred: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()