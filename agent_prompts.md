#Prompt 1: Main prompt
"Act as a senior Python developer.
Create a small Python project that calls the Open-Meteo API, fetches current weather data,
validates required fields, and saves a summary JSON file.

Provide:
- Folder structure
- main.py code
- a helper module
- input/output examples
- error handling logic
- a simple test file using pytest
- steps to run

Keep the code clean and well commented."

#Prompt 2: Generate API client"
"Write an api_client.py with a function get_weather_data(lat, lon)
using requests. Add proper exceptions and validation."

#Prompt 3: Summarisation logic
"Write a summarize_weather(data) function that extracts:
temperature, windspeed, winddirection, time
and returns a dictionary."

#Prompt 4: Main runner
"Now generate main.py that:
- reads city from user input
- finds coordinates (hardcode 5 cities or use a dictionary)
- calls API
- prints summary
- saves summary to JSON file"

#Prompt 5: Basic tests
"Generate pytest-based tests for:
- get_weather_data mocked response
- summarize_weather valid data
- handling missing fields"

#README Generation Prompt
"Act as a senior Python architect and technical documentation expert.

I already have an existing README.md in this project.
I want you to update and improve it, NOT replace it entirely.

Follow this process:

1. Read and analyse the existing README.md text.
2. Preserve all correct project info, naming, structure, setup steps, logic, and any specific terminology already used in the file.
3. Improve organisation, structure, formatting, grammar, and clarity.
4. Expand sections where details are missing:
    - Overview / Problem statement
    - Features
    - Technical approach
    - High-level design
    - Folder structure
    - Setup and run instructions
    - API usage explanation
    - Input/Output examples
    - Test coverage instructions
    - Assumptions
    - Edge cases, limitations
    - Future improvements
5. Integrate missing details from the codebase if needed (e.g., extracted from source files).
6. Add a short test scenario table at the end:
   | Scenario | Steps | Expected Result |

Additional rules:
- Keep the README professional and concise.
- Ensure all headings are well-structured using Markdown conventions.
- Use correct content based on the actual code in the repository.
- DO NOT remove valid existing content unless it is duplicated, unclear, or technically wrong.
- DO NOT add generic boilerplate text that does not match this project.
- Improve but do not change the intent or meaning of existing points.

Final output should be the revised README.md content only.
Do not include commentary or explanations outside the README text.

Below is the current README.md content:
<PASTE EXISTING README HERE>
"
