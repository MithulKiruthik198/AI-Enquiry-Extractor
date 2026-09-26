import os
import json
from typing import Literal

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field, ValidationError


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# Pydantic validation model
class Enquiry(BaseModel):
    name: str
    phone: str = Field(pattern=r"^\d{10}$")
    intent: str
    urgency: Literal["high", "medium", "low"]


# Read customer messages and save valid results
with open("samples.jsonl", "r") as file, open("results.jsonl", "a") as output_file:

    for line in file:
        data = json.loads(line)

        print("\nCustomer:")
        print(data["message"])

        prompt = f"""
You are a customer enquiry extraction system.

Extract:
- name
- phone
- intent
- urgency

Rules:
- If phone number is not provided, return null.
- urgency must be high, medium, or low.
- Return only valid JSON.
- Do not use Markdown.
- Do not add explanations.

Customer message:
{data["message"]}
"""

        try:
            for attempt in range(3):

                print(f"\nAttempt {attempt + 1}/3")

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

                text = response.text.strip()

                if text.startswith("```json"):
                    text = text[7:-3].strip()

                result = json.loads(text)

                if result.get("urgency"):
                    result["urgency"] = result["urgency"].lower()

                try:
                    validated = Enquiry(**result)

                    print("\n✅ Pydantic Validated:")
                    print(validated)

                    output_file.write(
                        validated.model_dump_json() + "\n"
                    )

                    print("✅ Saved successfully")

                    break

                except ValidationError as e:
                    print(f"\n❌ Validation failed on attempt {attempt + 1}")
                    print(e)

                    if attempt < 2:
                        prompt += f"""

Your previous output failed validation.

Validation error:
{e}

Return corrected JSON only.
"""

            else:
                print("\n❌ Failed after 3 attempts")

        except json.JSONDecodeError as e:
            print("\n❌ JSON Error:")
            print(e)

        except Exception as e:
            print("\n❌ AI Error:")
            print(e)