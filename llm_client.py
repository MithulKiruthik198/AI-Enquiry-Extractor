import os
import time
import logging
from dotenv import load_dotenv
from google import genai
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def ask_gemini(prompt):
    logging.info("Starting Gemini request")
    for attempt in range(3):
        try:
            start_time = time.time()
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            elapsed = time.time() - start_time
            print(f"Gemini response time: {elapsed:.2f} seconds")
            logging.info(f"Gemini request succeeded | latency={elapsed:.2f}s")
            return response
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

            status_code = getattr(e, "code", None)
            print(f"Error code: {status_code}")

            if status_code in [429, 503] and attempt < 2:
                wait_time = 2 ** attempt
                print(f"Retryable error {status_code}. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Non-retryable error {status_code}. Stopping.")
                return None

    print("Gemini failed after 3 attempts.")
    return None
if __name__ == "__main__":
    response = ask_gemini("""You are a customer enquiry extraction system.

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
- Do not add explanations..""")
    if response is None:

       print("No respone from AI LLM")
    else:
        print(response.text)