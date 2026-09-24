AI Enquiry Extractor

A Python project for building an AI-powered system that converts messy customer enquiries into structured information.

Example

A customer may send:

"Bro naan Suresh, my number 9876543212. Bike service venum, romba urgent."

The goal is to extract useful information such as:

{
  "name": "Suresh",
  "phone": "9876543212",
  "intent": "Bike service",
  "urgency": "high"
}

Current Progress

Completed

Python project setup

Virtual environment (.venv)

Environment variables using .env

API key handling

.gitignore for protecting secret files

Gemini API client setup

JSONL file creation

Reading JSONL data with Python

Using json.loads()

Working with Python dictionaries

Accessing dictionary values using keys

Looping through multiple customer enquiries

Connecting customer data to an LLM request

Current Pipeline

Customer enquiries
        ↓
    samples.jsonl
        ↓
      Python
        ↓
   Read each line
        ↓
 Python dictionary
        ↓
    Customer message
        ↓
       LLM

Project Files

AI Enquiry Extractor/
│
├── extractor.py
├── samples.jsonl
├── .env
├── .gitignore
└── README.md

File Description

extractor.py
Main Python program.

samples.jsonl
Contains sample customer enquiries, with one JSON object per line.

.env
Stores the API key locally.

.gitignore
Prevents sensitive and unnecessary files such as .env and .venv from being uploaded to GitHub.

What I Learned

Environment Variables

Used .env to keep API credentials outside the Python source code.

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

API Client

Created a client using the API key:

client = genai.Client(api_key=api_key)

The client provides the interface through which Python communicates with the AI API.

JSONL Processing

Read customer enquiries one line at a time:

with open("samples.jsonl", "r") as file:
    for line in file:
        data = json.loads(line)

Dictionary Access

Extracted the customer's message:

data["message"]

API Status

The Gemini model used during development returned a 503 UNAVAILABLE response because the model was temporarily experiencing high demand.

The Python project structure and JSONL processing can still be developed independently of the temporary model availability issue.

Next Steps

Build a strong extraction prompt

Extract name, phone, intent, and urgency

Return structured JSON from the LLM

Validate AI-generated data using Python

Handle missing or invalid information

Add error handling

Process 20+ customer enquiries

Save extracted results to results.jsonl

Test and improve failed cases

Complete the end-to-end AI enquiry pipeline

Goal

Build a small but practical AI system that can take messy real-world customer messages and convert them into reliable structured