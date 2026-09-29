import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def ask_gemini(prompt):
    for attempt in range(3):
        try:
            start_time = time.time()
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            elapsed = time.time() - start_time
            print(f"Gemini response time: {elapsed:.2f} seconds")

            return response
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < 2:
                wait_time = 2 ** attempt
                print(f"Waiting {wait_time} seconds...")
                time.sleep(wait_time)

    print("Gemini failed after 3 attempts.")
    return None
if __name__ == "__main__":
    response = ask_gemini("Say hello in one sentence.")
    if response is None:

       print("No respone from AI LLM")
    else:
        print(response.text)