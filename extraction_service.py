
import json
from llm_client import ask_gemini
from enquiry_models import Enquiry


def extract_enquiry(message: str):
    prompt = f"""
You are a customer enquiry extraction system.

Extract these fields:
- name
- phone
- intent
- urgency

Rules:
- If name or phone is missing, return null.
- urgency must be high, medium, or low.
- Return only valid JSON.
- Do not use Markdown or explanations.

Customer message:
{message}
"""

    response = ask_gemini(prompt)

    if response is None or not response.text:
        raise RuntimeError("Gemini did not return a response.")

    result = json.loads(response.text)
    validated = Enquiry(**result)
    return validated.model_dump()