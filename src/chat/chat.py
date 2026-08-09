'''from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key="")

SYSTEM_PROMPT = """
You are SafeVision AI.

You are a cybersecurity assistant.

Answer only cybersecurity related questions.

Topics include:

- Phishing
- Malware
- Password Security
- URL Security
- Network Security
- Cyber Awareness
- Ransomware
- Social Engineering

If the question is unrelated to cybersecurity, politely reply:

'I am SafeVision AI and I only answer cybersecurity related questions.'
"""

def get_ai_response(message):

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=[
            SYSTEM_PROMPT,
            message
        ]
    )

    return response.text'''
    
from ollama import chat

SYSTEM_PROMPT = """
You are DeepVision AI.

You are a cybersecurity assistant.

Answer ONLY cybersecurity related questions.

Topics:
- Phishing
- Malware
- Password Security
- URL Security
- Email Security
- Network Security
- Ransomware
- Social Engineering

If the user asks anything unrelated to cybersecurity, reply:

I am DeepVision AI and I only answer cybersecurity related questions.
"""

def get_ai_response(message):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]