import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

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

Return only valid JSON.

Customer message:
{data["message"]}
"""

        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            print("\nAI Result:")
            print(repr(response.text))

            text = response.text.strip()

            if text.startswith("```json"):
                text = text[7:-3].strip()

            result = json.loads(text)

            print("\nPython Dictionary:")
            print(result)

            if result["name"] is None:
                print("Invalid: name is missing")

            phone = str(result.get("phone", ""))

            if not phone.isdigit() or len(phone) != 10:
                print("Invalid: phone number")

            output_file.write(json.dumps(result) + "\n")

        except Exception as e:
            print("\nAI Error:")
            print(e)