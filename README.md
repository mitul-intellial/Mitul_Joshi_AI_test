✦ Command-Line Weather App

  A simple Python-based command-line application to fetch, summarize, and save the current weather for a predefined list of major cities, created within the Mitul_Joshi_AI_test
  project.

  1. Overview


  This project provides a simple and efficient way for a user to retrieve the current weather conditions for a specific city directly from their terminal. The application is
  designed to be easy to set up and run, handle potential network errors gracefully, and present the weather information in a clean, human-readable format. The resulting summary is
  also persisted to a JSON file for programmatic access.

  2. Key Features


   * Interactive CLI: Prompts the user to enter a city name from a predefined list.
   * Real-time Weather Data: Fetches current weather from the live Open-Meteo public API.
   * Clean Data Summary: Extracts and displays the most relevant weather metrics (temperature, wind speed, etc.).
   * JSON Output: Saves the latest weather summary to a weather_summary.json file.
   * Modular Architecture: Code is logically separated into modules for API communication, data processing, and application logic.
   * Robust Error Handling: Gracefully manages invalid user input and API/network failures.
   * Comprehensive Test Suite: Includes unit tests with mocked dependencies to ensure reliability.

  3. Technical Approach and High-level Design

  The application follows a modular architecture to separate concerns:


   1. Presentation Layer (`main.py`): The main entry point and user interface. It handles user input, orchestrates calls to the other modules, formats the final output for the console,
      and saves the results to a file.


   2. API Client Layer (`api_client.py`): This module is solely responsible for external API communication. It contains the get_weather_data function, which constructs the API request,
      sends it using the requests library, and performs validation and error handling on the response.


   3. Data Processing Layer (`helper.py`): This module contains the summarize_weather utility function. Its purpose is to transform the raw JSON data from the API into a clean,
      simplified dictionary.


  The data flows from user input in main.py, to a coordinate lookup, to a request in api_client.py, back to main.py, through helper.py for processing, and is finally printed to the
  console and saved to weather_summary.json.

  4. Folder Structure



    1 E:/Mitul_Joshi_AI_test/
    2 ├── .git/
    3 ├── README.md
    4 ├── weather_summary.json
    5 └── weather_app/
    6     ├── __init__.py
    7     ├── api_client.py
    8     ├── helper.py
    9     ├── main.py
    10    ├── requirements.txt
    11    └── tests/
    12        ├── __init__.py
    13        ├── test_api_client.py
    14        └── test_helper.py



  5. Setup and Installation

  Prerequisites
   * Python 3.10 or newer.
   * pip for installing packages.


  Installation Steps
   1. Clone the repository to your local machine.
   2. Navigate to the project's root directory.
   3. Install the required packages from the requirements.txt file:
   1     pip install -r weather_app/requirements.txt


  6. How to Run the Program


  Execute the main.py script from the project's root directory. The program will prompt you to enter the name of a city.

  Sample Command

   1 python weather_app/main.py


  Expected Console Output


    1 Enter a city name: london
    2 Fetching weather for London (Lat: 51.51, Lon: -0.13)...
    3 
    4 --- Weather Summary ---
    5 Temperature: 15.0
    6 Windspeed: 5.5
    7 Winddirection: 270
    8 Time: 2025-12-01T14:00
    9 -----------------------
    10 
    11 Summary saved to E:\Mitul_Joshi_AI_test\weather_summary.json



  7. API Usage Details

  The application uses the Open-Meteo Weather Forecast API, a free service that does not require an API key.


   * Endpoint: https://api.open-meteo.com/v1/forecast
   * Query Parameters:
       * latitude: The latitude for the location (e.g., 51.51).
       * longitude: The longitude for the location (e.g., -0.13).
       * current_weather=true: A flag to request the current weather conditions.
   * Sample Response Structure: The application parses the current_weather object from the API's JSON response.



    1     {
    2       "current_weather": {
    3         "temperature": 15.0,
    4         "windspeed": 5.5,
    5         "winddirection": 270,
    6         "time": "2025-12-01T14:00"
    7       }
    8     }


  8. Input and Output Examples


  User Input
  The user provides one of the supported city names (case-insensitive) at the prompt.

   1 Enter a city name: paris


  Console Output
  A formatted summary is printed to the console.



    1 --- Weather Summary ---
    2 Temperature: 18.2
    3 Windspeed: 8.1
    4 Winddirection: 245
    5 Time: 2025-12-01T18:00
    6 -----------------------


  File Output (weather_summary.json)
  The summary is saved as a formatted JSON file in the project root.



    1 {
    2     "temperature": 18.2,
    3     "windspeed": 8.1,
    4     "winddirection": 245,
    5     "time": "2025-12-01T18:00"
    6 }


  9. Test Coverage


  Test Structure
  Tests are located in the weather_app/tests/ directory and use the pytest framework.
   * test_api_client.py: Unit tests for the API communication layer, using unittest.mock to simulate API responses and network failures.
   * test_helper.py: Unit tests for the data processing functions, ensuring they handle both valid and malformed data structures.

  How to Run Tests
  To run the full test suite, navigate to the project root directory and execute the following command, which is more reliable than a direct pytest call:

    1 python -m pytest



  10. Assumptions and Design Decisions


   * Hardcoded City Coordinates: To avoid the complexity of an external geocoding API, a dictionary of 5 major cities and their coordinates is hardcoded.
   * Single File Output: The application overwrites weather_summary.json on each run and does not maintain a history of weather queries.
   * Error Messaging: Errors are printed directly to the console for immediate user feedback rather than being logged to a separate file.

  11. Limitations and Edge Cases


   * Limited City Support: The application only supports the 5 cities hardcoded in main.py. Any other city name will result in an error.
   * No API Fallback: If the Open-Meteo API is down or unreachable, the program will fail and cannot provide weather data.
   * Redundant Code: The helper.py module contains a legacy get_weather_data function that is not used by the main application flow. This could be a source of confusion and should be
     removed in a future iteration.

  12. Future Improvements


   * Dynamic City Geocoding: Integrate a free geocoding API (e.g., Nominatim) to look up coordinates for any city name provided by the user.
   * Configuration File: Move hardcoded values like the city list into a configuration file (e.g., config.ini) to make them easier to modify without changing the code.
   * Code Refactoring: Remove the unused get_weather_data function from helper.py to eliminate redundancy.
   * Structured Logging: Implement Python's built-in logging module to create structured logs that can be written to a file for easier debugging.

  ---

  High-Level Test Scenarios



    | Scenario                  | Steps                                                              | Expected Result
                             |
    | ------------------------- | ------------------------------------------------------------------ |
    ----------------------------------------------------------------------------------------------------------- |
    | Successful Weather Query  | 1. Run python weather_app/main.py.<br>2. Enter london.         | The terminal prints a formatted weather summary for London, and weather_summary.json
    is created/updated.  |
    | Invalid City Input      | 1. Run python weather_app/main.py.<br>2. Enter madrid.          | The terminal prints an error message stating the city is not found and lists the
    available cities.          |
    | Case-Insensitive Input  | 1. Run python weather_app/main.py.<br>2. Enter NEW YORK.        | The application correctly identifies "new york" and returns its weather summary.
                        |
    | API or Network Failure  | 1. Disconnect from the internet.<br>2. Run the program and enter a valid city. | The terminal prints a clear error message indicating that the API
    request failed due to a network issue.      |
    | Scenario                  | Steps                                                              | Expected Result