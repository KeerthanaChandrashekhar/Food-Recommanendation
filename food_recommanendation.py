import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found! Set GEMINI_API_KEY as an environment variable.")
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)