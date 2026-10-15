# AI Enquiry Extractor

I'm building this project to learn how AI can be used to solve a real-world problem using Python.

When customers send messages, they don't always explain their requirements in a structured way. They might mix languages, use informal words, or mention several details in a single message. Finding the important information manually can take time.

The idea behind this project is simple: take a customer message and extract the useful details into a structured format.

## Example

A customer might send a message like this:

> Bro naan Suresh, my number 9876543212. Bike service venum, romba urgent.

Instead of keeping the entire message as plain text, I want the system to extract the important information:

```json
{
  "name": "Suresh",
  "phone": "9876543212",
  "intent": "Bike service",
  "urgency": "high"
}
```

This is an example of the expected output. The actual result depends on how the AI interprets the message.

## What I've built so far

I started with basic Python code for reading customer enquiries from a JSONL file. From there, I worked on connecting the messages to Gemini and extracting information from them.

As the project grew, I added a few more things:

- A Gemini API client for communicating with the AI model.
- A Pydantic model to validate the extracted information.
- An extraction service to handle the AI response and convert it into structured data.
- A FastAPI application with endpoints for checking the API status and extracting enquiries.
- Automated tests using pytest to check whether the validation and extraction logic behave as expected.

I'm building this step by step, so there are still parts that need improvement.

## How it works

The basic flow is:

```text
Customer message
       ↓
   FastAPI API
       ↓
 Extraction service
       ↓
    Gemini AI
       ↓
    JSON data
       ↓
 Pydantic validation
       ↓
 Structured response
```

The goal is to make the output predictable enough for another application to use.

## Project structure

```text
AI-Enquiry-Extractor/
│
├── main.py
├── extraction_service.py
├── enquiry_models.py
├── llm_client.py
├── extractor.py
│
├── test_enquiry_models.py
├── test_extraction_service.py
│
├── samples.jsonl
├── results.jsonl
├── requirements.txt
├── .gitignore
└── README.md
```

A quick look at the main files:

- `main.py` — The FastAPI application and its endpoints.
- `extraction_service.py` — Handles extraction, JSON parsing, and validation.
- `enquiry_models.py` — Defines the structure of an enquiry and its validation rules.
- `llm_client.py` — Handles communication with Gemini.
- `extractor.py` — The batch-processing script.
- `test_enquiry_models.py` — Tests the enquiry model.
- `test_extraction_service.py` — Tests the extraction service without making real Gemini requests for the mocked test cases.

## Running the project

You'll need Python, a Gemini API key, and the packages listed in `requirements.txt`.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/ai-enquiry-extractor.git
cd ai-enquiry-extractor
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a `.env` file in the project folder and add your API key:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Keep this file private. It should never be pushed to GitHub.

Start the API:

```powershell
python -m uvicorn main:app --reload
```

The API runs locally at `http://127.0.0.1:8000`.

You can open `http://127.0.0.1:8000/docs` to try the endpoints.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Checks whether the API is running |
| GET | `/version` | Returns the current version |
| POST | `/extract` | Extracts information from a customer message |

## Testing

I'm using pytest to check that the project behaves correctly, including when it receives invalid data.

Run the tests with:

```powershell
python -m pytest -v
```

The current test suite has **7 passing tests**. They cover valid enquiry data, invalid phone numbers, invalid urgency values, malformed JSON, and extraction using simulated Gemini responses.

These tests help me catch problems without having to make a real API request every time.

## What I'm learning

While working on this project, I've been learning how to:

- Organize Python code into separate modules.
- Read and process JSONL files.
- Work with APIs and environment variables.
- Use an LLM to extract information from natural-language messages.
- Validate AI-generated data using Pydantic.
- Build API endpoints with FastAPI.
- Handle errors and write automated tests.

## What's next?

I want to make the project more reliable before considering it finished.

My next steps are to improve error handling, test more types of customer messages, evaluate how accurately the model extracts information, and test Tamil and Tanglish messages systematically. I also want to improve batch processing and make the project easier for someone else to set up and run.

This is an ongoing project, and I'm using it to understand not just how to call an AI API, but how to build a complete application around it.

 About me

I'm Mithul Kiruthik, a student interested in Python, AI, and building useful software. I'm learning by building projects, testing what I write, and improving the code as I go.

GitHub: [MithulKiruthik198](https://github.com/MithulKiruthik198)