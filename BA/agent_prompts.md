#Prompt 1: Clarify the Problem & Goals
"Act as a senior business analyst.

I am working on a small project that uses an external API (for example a weather API or similar public API).
My goal is to:
- define the problem statement
- identify key users/personas
- describe the main use cases
- clarify the business goals and success metrics

Ask me 5–7 focused clarification questions first.
Then, based on my answers, draft:
- a clear problem statement
- 2–3 primary personas
- 4–6 high-level use cases

Wait for my answers before drafting anything."

#Prompt 2: Generate Functional Requirements
Based on the following context and problem statement, help me define functional requirements.

Context:
[PASTE problem statement, personas, and use cases here]

Act as a business analyst.

1. Group the functional requirements by feature area.
2. Write them as clear, testable statements (e.g. "The system shall …").
3. Number them (FR-01, FR-02, …).
4. Keep the list realistic for a 2–3 hour assessment scope.

Output only a Markdown list of functional requirements.

#Prompt 3: Non-Functional Requirements
Using the same context as above, now propose non-functional requirements (NFRs) relevant to a small API-based tool.

Include aspects like:
- performance
- reliability / error handling
- usability
- security (basic)
- logging / monitoring

Format them as:
- NFR-01: [statement]

Make them realistic for a small internal prototype.

#Prompt 3: API Contract Draft
Act as a business analyst collaborating with developers and API integrators.

We are building a feature that consumes an external API to provide weather insights to users.

Define a proposed API contract for our internal service (not the external provider):
- request structure (fields, types, example)
- response structure (fields, types, example)
- key validation rules
- typical error responses and error codes

Format the result as:
- Request schema (table)
- Response schema (table)
- Error scenarios (table: Code, Condition, Message, Handling)

Keep it concise but precise.

#Prompt 4 – User Flow / Journey
Using the functional requirements defined earlier, act as a BA and describe the end-to-end user journey for the main scenario.

For example:
- User enters a city or some input
- System calls the external API
- System validates, transforms, and displays results
- Errors/edge cases are handled

Provide:
1. A step-by-step flow (numbered steps).
2. A simple text-based flow diagram using Markdown (e.g. User -> System -> API -> System -> User).
3. Highlight at which steps validation and error handling occur.


#Prompt 5 – Acceptance Criteria (per requirement)
Act as a BA with QA mindset.

Using the functional requirements list below:
[  * FR-01: The system shall fetch data from a predefined external API endpoint based on user input.
   * FR-02: The system shall process the raw API data to extract a specific, predefined set of summary fields (e.g., temperature, wind speed, time).
   * FR-03: The system shall display the extracted summary data in a human-readable format on the command line.

  Data Output and Persistence


   * FR-04: The system shall save the extracted summary data to a single, structured JSON file in the project's root directory.
   * FR-05: The system shall overwrite the JSON file with the latest summary upon each successful execution.

  User Input and Interaction


   * FR-06: The system shall accept a single text string from the command-line prompt as its primary input.
   * FR-07: The system shall maintain a hardcoded, case-insensitive list of supported text inputs (e.g., a list of specific cities).]

For each key requirement, write 2–4 acceptance criteria using a clear format.
Prefer "Given/When/Then/Steps/Expected Result" or bullet-point criteria.

Output format:
- FR-01: [short title]
  - AC-01.1: Given… When… Then… Steps… Expected Result…
  - AC-01.2: …

Focus on realistic, testable behaviour and include at least some negative / error cases.

#Prompt 6 – Test Scenarios Table
Now, based on the acceptance criteria above, create a compact test scenario table for the main flows.

Format as Markdown:

| ID | Scenario | Precondition | Steps | Expected Result |

Include:
- normal successful flow
- invalid input
- API failure / timeout
- unexpected/missing fields in API response (if applicable)

#Prompt 7 – Assumptions & Edge Cases
Act as a senior BA.

For this API-based tool, list:

1. Assumptions (about users, API availability, data correctness, supported inputs, etc.)
2. Edge cases to consider (e.g. no data for city, extreme values, API limits, timeouts).
3. Open questions that should be clarified with product owner or tech lead.

Output as three separate Markdown lists with clear bullets.

#Prompt 8 – Risk Analysis (Optional but Strong)
Using the same context, identify 5–10 key risks related to:
- external API dependency
- data quality
- usability
- performance
- maintainability

For each risk, provide:
- Risk ID
- Description
- Impact (Low/Medium/High)
- Likelihood (Low/Medium/High)
- Suggested mitigation

Output as a Markdown table.

Prompt 9 – BA Section for README
Act as a business analyst.

I want to add a "Business Analysis" section to my project README.md to explain the feature from a BA perspective.

Using the requirements, flows, and test scenarios we defined, create a concise BA section that includes:

1. Problem statement and goals (2–3 short paragraphs)
2. Target users and key use cases (bullet list)
3. Summary of main functional and non-functional requirements
4. Reference to acceptance criteria and test scenarios
5. Brief note on assumptions and limitations

Keep it clear, structured, and not too long. Output in Markdown so I can paste it directly into README.
