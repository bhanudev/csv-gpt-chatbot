# openai_chat.py

import os
from openai import OpenAI
from openai.types import APIError, RateLimitError

# Create the client using the environment variable (set in app.py)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(prompt, context):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a helpful data analyst. Answer based on the provided CSV content."},
                {"role": "user", "content": f"Here is the CSV data:\n\n{context}\n\nQuestion: {prompt}"}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        return "⚠️ OpenAI API quota exceeded. Please check your billing and usage."

    except APIError as e:
        return f"❌ OpenAI API error: {str(e)}"

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"
