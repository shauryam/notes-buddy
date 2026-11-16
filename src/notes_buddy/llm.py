import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

ai_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def call_llm(model: str, messages: list):

    response = ai_client.chat.completions.create(
        model=model,
        messages=messages
    )
    
    print(response.choices[0].message.content)
    return response
