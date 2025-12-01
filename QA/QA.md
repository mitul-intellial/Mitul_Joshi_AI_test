Scope of Testing
   * The system must accept a valid, supported text input from a user, fetch data from the external API, and display a formatted summary to the console.
       * Relevant Tests: Functional Testing, End-to-End (E2E) Testing.


   * The system must reject any user input that is not in the predefined list of supported items and respond with a clear error message that guides the user.
       * Relevant Tests: Negative Functional Testing, Error Handling, Usability Testing.


   * The system must correctly handle various external API responses, including network failures, timeouts, and HTTP error codes (e.g., 4xx, 5xx), without crashing.
       * Relevant Tests: Error Handling, Reliability Testing, Integration Testing.


   * The system must accurately parse the raw JSON response from the API, extract the correct data fields, and handle cases where expected fields are missing or null.
       * Relevant Tests: Data Validation Testing, Error Handling.

   * The system must generate a structured JSON file containing the summarized data and ensure this file is correctly overwritten upon subsequent successful runs.    
       * Relevant Tests: File Output Validation, Data Integrity Testing.


   * The application must be executable from a command-line script and produce a consistent, machine-readable JSON output file that can be used in automated workflows.
       * Relevant Tests: E2E Testing, Usability Testing (for developers/analysts).

Test Strategy
  In-Scope Test Types


   * Functional Testing: Verifying the "happy path" where a user provides a valid input, and the system successfully fetches, processes, displays, and saves the data as expected.     
   * Negative Testing: Challenging the system with invalid inputs (e.g., unsupported city names, empty strings) to ensure it handles them gracefully and provides clear, helpful error 
     messages.
   * Error Handling & Reliability Testing: Simulating external failures, such as API timeouts, network disconnections, or HTTP error codes (4xx/5xx), to ensure the application reports
     these issues correctly without crashing.
   * Data Validation Testing: Ensuring the data extracted from the API response is correct and that the final JSON output file is well-formed and contains the expected information.   
   * Basic Performance Testing: Measuring the end-to-end response time for a typical request to ensure it meets the user expectation of being an "instant" utility.
   * Basic Usability Testing: Assessing the clarity of instructions, console output, and error messages from the perspective of a technical user.

  Out-of-Scope Items


   * Load and Stress Testing: The tool is a single-user CLI utility, so testing with concurrent users or under heavy load is not required for this assessment.
   * Comprehensive Security Testing: While basic validation will be checked, a full security or penetration test is out of scope for this internal tool.
   * Extensive Compatibility Testing: Testing will be limited to a modern Python version on a standard developer environment. We will not test across a wide matrix of different     
     operating systems or Python versions.
   * External API Validation: We will not test the external API provider for the accuracy of its weather data; we will only test our system's ability to correctly handle the data it
     provides.

  Test Levels


   * Unit Tests: Developers will be responsible for writing unit tests to cover individual functions, especially the data transformation logic (summarize_weather) and the API client's
     request formatting. The external API will be mocked at this level.
   * Integration Tests: A small set of automated or semi-automated tests will be run against the live external API to verify the end-to-end connection and ensure our parsing logic    
     works with real-world responses. These will be run sparingly to avoid hitting rate limits.
   * Manual & Exploratory Checks: QA will perform manual end-to-end tests of the compiled application to verify the user journey, check the usability of the CLI, and explore edge     
     cases not covered by automation.

  Test Data Approach


   * Input Data: A defined set of valid inputs (the hardcoded city list) and invalid inputs (unsupported cities, special characters, empty strings) will be used.
   * Mocked API Data: For unit tests, we will use static JSON files that simulate various API responses: a successful response, a response with missing/null fields, and error
     responses.
   * Live Data: Manual and integration tests will use the real-time data returned from the live API to validate the system against actual conditions.

  Risks & Areas Needing More Attention


   * External API Dependency: This is the highest-risk area. All error handling related to API availability, timeouts, and unexpected status codes must be a primary focus of testing.
   * Data Transformation Logic: The function that parses the API response is critical. It must be robustly tested against malformed or incomplete data to prevent the application from
     crashing.
   * File Output: The process of writing the JSON file could fail due to file system permissions. This error path must be explicitly tested.


Test Scenarios
   * TS-01: Successful end-to-end flow with valid input.
       * Verify that when a user enters a valid, supported city name, the system fetches data, displays a correctly formatted summary to the console, and creates a valid JSON file
         with the same data.
       * Maps to: FR-01, FR-02, FR-03, FR-04, FR-06, FR-07


   * TS-02: Verify case-insensitive input handling.
       * Verify that entering a supported city name with varied casing (e.g., "LoNdOn", "new york") is processed successfully, yielding the same result as the standard lowercase
         input.
       * Maps to: FR-07


   * TS-03: Handle unsupported city input.
       * Verify that when a user enters a city name not present in the hardcoded list, the system displays a clear error message and does not attempt to call the API.
       * Maps to: FR-07


   * TS-04: Handle empty or whitespace input.
       * Verify that if the user provides an empty string or only whitespace as input, the system shows a relevant error message and terminates gracefully.
       * Maps to: FR-06


   * TS-05: Handle external API failure.
       * Verify that if the external API is unavailable (e.g., returns a 503 error or times out), the system displays a user-friendly error message about the service failure and does
         not produce an output file.
       * Maps to: FR-01


   * TS-06: Handle unexpected API response structure.
       * Verify that if the API returns a success status (200 OK) but the JSON response is missing expected fields, the system handles it without crashing (e.g., by displaying "N/A"
         for missing values).
       * Maps to: FR-02

   * TS-07: Verify file overwrite functionality.
       * Verify that after running the application successfully for one city, running it again for a different city correctly overwrites the contents of the existing JSON file with 
         the new data.
       * Maps to: FR-05


   * TS-08: Handle file system permission error.
       * Verify that if the application does not have permission to write to the target directory, it displays an appropriate error message to the user instead of crashing.
       * Maps to: FR-04

Detailed Test Case Table
  TS-01: Successful End-to-End Flow


   * TC-1.1: Basic Success Case: Verify that entering a simple, single-word city name (london) successfully displays a summary and creates a correct JSON file.
   * TC-1.2: Multi-Word Input: Verify that entering a supported city with a space in its name (new york) is handled correctly.
   * TC-1.3: Console Output Formatting: Verify that the console output is formatted exactly as specified (e.g., labels, units, line breaks are correct).
   * TC-1.4: JSON File Structure: Verify that the generated weather_summary.json file is a well-formed JSON object and contains the exact keys and data types defined in the
     requirements.
   * TC-1.5: Initial File Creation: Verify that if weather_summary.json does not exist, it is created successfully on the first valid run.

  TS-02: Case-Insensitive Input Handling


   * TC-2.1: All Lowercase: Verify a valid city in all lowercase (paris) is successful.
   * TC-2.2: All Uppercase: Verify a valid city in all uppercase (PARIS) is successful.
   * TC-2.3: Mixed Case: Verify a valid city in mixed case (pArIs) is successful.
   * TC-2.4: Title Case: Verify a valid city in title case (Paris) is successful.
   * TC-2.5: Multi-Word Mixed Case: Verify a multi-word city with mixed casing (nEw YoRk) is successful.

  TS-03: Unsupported City Input


   * TC-3.1: Plausible but Unsupported City: Verify that entering a real city that is not on the supported list (berlin) results in the "unsupported" error message.
   * TC-3.2: Input with Numbers: Verify that entering an alphanumeric string (city123) results in the "unsupported" error message.
   * TC-3.3: Input with Special Characters: Verify that entering a string with special characters (sydney!@#) results in the "unsupported" error message.
   * TC-3.4: Very Long String Input: Verify that entering a very long string (e.g., 200+ characters) is handled gracefully and shows the "unsupported" error.       
   * TC-3.5: Error Message Content: Verify that the error message for an unsupported city correctly lists all available, supported city names.


  TS-04: Empty or Whitespace Input


   * TC-4.1: Empty String: Verify that providing no input (pressing Enter at the prompt) results in a specific error message for empty input.
   * TC-4.2: Single Space: Verify that entering a single space character results in an error.
   * TC-4.3: Multiple Spaces: Verify that entering multiple space characters results in an error.
   * TC-4.4: Tab Character: Verify that entering a tab character results in an error.
   * TC-4.5: No File Creation: Verify that no output file is created or modified when the input is empty or whitespace.

  TS-05: External API Failure


   * TC-5.1: API Timeout: (Requires simulation) Verify that if the API takes longer than the defined timeout to respond, the application shows a timeout-specific error message.  
   * TC-5.2: API Server Error (5xx): (Requires simulation) Verify that if the API returns a 500 or 503 error, the application displays a "service unavailable" message.
   * TC-5.3: API Client Error (4xx): (Requires simulation) Verify that if the API returns a 404 (Not Found) or 400 (Bad Request), the application displays a generic but clear API
     error message.
   * TC-5.4: DNS Failure: (Requires simulation) Verify that if the API's domain cannot be resolved, a network-related error message is shown.
   * TC-5.5: No Output on Failure: Verify that in all API failure scenarios, the weather_summary.json file is not created or altered.

  TS-06: Unexpected API Response Structure


   * TC-6.1: Empty JSON Response: (Requires simulation) Verify the system handles a 200 OK response with an empty JSON object ({}) without crashing.
   * TC-6.2: Core Object Missing: (Requires simulation) Verify the system handles a response where the current_weather object is missing entirely.
   * TC-6.3: Partial Data (Field Missing): (Requires simulation) Verify that if current_weather is present but a key like wind_speed is missing, the output displays a placeholder for
     that value.
   * TC-6.4: Null Data Values: (Requires simulation) Verify that if a key has a null value (e.g., "temperature": null), the output displays a placeholder for that value.
   * TC-6.5: Incorrect Data Type: (Requires simulation) Verify the system's behavior if a field has an incorrect data type (e.g., "temperature": "hot"). It should ideally handle this
     gracefully without crashing.

  TS-07: File Overwrite Functionality


   * TC-7.1: Standard Overwrite: Run for City A, then for City B. Verify the file contains only City B's data.
   * TC-7.2: Overwrite with Same City: Run for City A, then run again for City A. Verify the file is correctly updated with the new data for City A.
   * TC-7.3: No Overwrite on Failure: Run for City A, then trigger a failed run (e.g., invalid city). Verify the file still contains the original data for City A.   
   * TC-7.4: Re-creation After Deletion: Run for City A, manually delete the output file, then run for City B. Verify the file is created again with City B's data.  
   * TC-7.5: Overwrite with Empty Result: (Edge case) If a valid API response resulted in an "empty" summary, verify the file is overwritten with that empty summary.

  TS-08: File System Permission Error


   * TC-8.1: Read-Only Directory: (Requires setup) Set the output directory to be read-only. Run the application with a valid city. Verify a clear file permission error is displayed.
   * TC-8.2: Read-Only File: (Requires setup) Create a read-only weather_summary.json file. Run the application. Verify a file permission error is displayed.
   * TC-8.3: Console Output on File Error: Verify that even if the file write fails, the weather summary is still correctly displayed on the console.
   * TC-8.4: Graceful Termination: Verify the application terminates gracefully after a file write error and does not crash.
   * TC-8.5: Invalid Path: (Edge case) If the output path is configured to be an invalid or non-existent directory, verify a clear error is shown.

Edge and Negative Tests
  1. Edge Cases for Input Values


   * Empty and Whitespace: Test with an empty string (user presses Enter immediately), a single space, multiple spaces, and tab characters as input.
   * Very Long Strings: Test with an input string that is excessively long (e.g., 500+ characters) to check for buffer overflows or unexpected truncation.
   * Special Characters and Injection: Test with inputs containing special characters (!@#$%^&*()), SQL-like syntax (' OR 1=1; --), and shell commands (london; ls) to ensure they are
     handled as simple strings and not executed or misinterpreted.
   * Unsupported but Similar Names: Test with a misspelled version of a supported city (e.g., "londn" instead of "london") and a valid city that is not on the supported list (e.g.,  
     "berlin").
   * Non-ASCII Characters: Test with city names containing international characters (e.g., "São Paulo", "München") to ensure correct handling of UTF-8 encoding.
   * Numeric Input: Test with input that is purely numeric ("12345") or alphanumeric ("paris2024").

  2. Negative Test Cases for API Behaviour


   * Request Timeout: Simulate a scenario where the external API takes longer than the application's configured timeout period to respond. The application should terminate gracefully 
     with a timeout error.
   * HTTP 5xx Server Errors: Simulate the API responding with 500 Internal Server Error and 503 Service Unavailable to verify the application displays a clear "service unavailable"   
     message.
   * HTTP 4xx Client Errors: Simulate the API responding with 401 Unauthorized (e.g., if it suddenly requires a key) or 429 Too Many Requests (rate limiting) to ensure these are      
     handled as distinct API errors.
   * Slow API Response: Test the user experience when the API responds just under the timeout threshold to check for perceived performance issues.
   * Connection Refused / DNS Failure: Simulate a complete network failure where the API's domain cannot be resolved or the connection is refused, ensuring a network-specific error is
     shown.

  3. Data Validation Checks on the Response


   * Missing Core Object: Test with a 200 OK API response where the entire current_weather JSON object is missing. The application should not crash and should report that the expected
     data was not found.
   * Missing Specific Fields: Test with a response where the current_weather object is present but is missing one or more key fields (e.g., no wind_speed). The output should show a   
     placeholder for the missing data.
   * Null Values: Test with a response where a required field has a null value (e.g., "temperature": null). The output should handle this gracefully.
   * Incorrect Data Types: Test with a response where a field has an incorrect data type (e.g., "temperature": "twenty" instead of a number). The application should ideally handle    
     this type mismatch without crashing.
   * Empty Response Body: Test with a 200 OK response that has an empty body or contains an empty JSON object ({}).

Manual Test Checklist
   - [ ] TC-01: Run with a valid, single-word city (e.g., london) and verify the console displays a correctly formatted weather summary.
   - [ ] TC-02: Following a successful run, verify that weather_summary.json is created in the root directory and its content matches the console output.
   - [ ] TC-03: Run with a valid, multi-word city (e.g., new york) and verify the console output is correct.
   - [ ] TC-04: Run with a supported city using mixed casing (e.g., pArIs) and verify the input is handled correctly and produces a successful result.
   - [ ] TC-05: Run with an unsupported city (e.g., berlin) and verify a clear error message is displayed.
   - [ ] TC-06: Verify the error message from an unsupported city input correctly lists all available, valid city options.
   - TC-07: Run with an empty string or only whitespace as input and verify a specific error message for invalid input is shown.
   - TC-08: After a failed run (due to invalid input), verify that weather_summary.json has not been created or modified.
   - TC-09: Run the tool for one city (london), then immediately run it again for a different city (tokyo), and verify the weather_summary.json file is overwritten with Tokyo's data.
   - TC-10: Disable the machine's network connection and run the tool with a valid city. Verify a clear network-related error message is displayed.
   - TC-11: Manually inspect the weather_summary.json file after a successful run and confirm it is well-formed JSON (e.g., using an online validator or code editor).
   - TC-12: On a successful run, verify that a confirmation message (e.g., "Summary saved to...") is printed to the console.
   - [ ] TC-01: Run with a valid, single-word city (e.g., london) and verify the console displays a correctly formatted weather summary.
   - [ ] TC-02: Following a successful run, verify that weather_summary.json is created in the root directory and its content matches the console output.
   - [ ] TC-03: Run with a valid, multi-word city (e.g., new york) and verify the console output is correct.