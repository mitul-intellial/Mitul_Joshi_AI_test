#Prompt 1 – QA View of Requirements
"Act as a QA engineer.

I have the following problem statement, personas, and high-level use cases for a small API-based utility:

--- CONTEXT START ---
[PASTE your Problem Statement, Personas, Use Cases]
--- CONTEXT END ---

1. Summarise the system behaviour from a QA perspective in 5–8 bullet points.
2. For each behaviour, mention what type of tests are most relevant (e.g. functional, negative, error-handling, data validation, file output, etc.).

Output only the bullet list."


#Prompt 2 – Test Strategy Outline
"Act as a senior QA engineer.

Based on the same context:

--- CONTEXT START ---
[PASTE same Problem Statement, Personas, Use Cases]
--- CONTEXT END ---

Define a high-level test strategy for this project including:

- In-scope test types (e.g. functional, negative, error-handling, basic performance, basic usability)
- Out-of-scope items (what will NOT be tested in this small assessment)
- Test levels (unit, integration, manual checks)
- Basic test data approach
- Risks or areas needing more attention

Keep it short and structured. Use Markdown headings and bullet points.
"

#Prompt 3 – Test Scenarios List
"Act as a QA engineer.

Using the following functional requirements:

--- CONTEXT START ---
[PASTE your FR-01, FR-02, etc.]
--- CONTEXT END ---

Generate a list of test scenarios.

Rules:
- Map each scenario to one or more FR IDs.
- Include both positive and negative scenarios.
- Use a short, clear description for each scenario.
- Prefix scenario IDs as TS-01, TS-02, etc.

Output in Markdown as a list.
"


#Prompt 4 – Detailed Test Case Table
Now, convert the test scenarios below into a detailed test case table:

--- CONTEXT START ---
[PASTE generated test scenarios TS-01, TS-02, …]
--- CONTEXT END ---

Use this table format in Markdown:

| ID | Scenario | Precondition | Test Steps | Test Data | Expected Result |
|----|----------|--------------|-----------|-----------|-----------------|

Include:
- successful data retrieval
- invalid input
- unsupported item
- API/network failure
- handling of malformed or missing response fields
- saving summary to file and verifying content.

Keep steps concise but clear.

#Prompt 5 – Edge and Negative Tests
Act as a QA engineer specializing in API and data validation.

Based on the same functional requirements and use cases, propose:

1. Edge cases for input values (e.g. empty, very long, special characters, unsupported but similar names).
2. Negative test cases specifically for API behaviour (e.g. timeouts, HTTP 4xx/5xx, slow responses, unexpected fields).
3. Data validation checks on the response (e.g. missing fields, null values, wrong types).

Format as three bullet lists. Each bullet should be a potential test idea.

#Prompt 6 – Manual Test Checklist
