#openai_chat.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(query, df_head):
    prompt = f"""
You are a data analyst. A user uploaded the following data:\n{df_head}\n
Answer their question based on this data: "{query}"
Only use the visible information, no assumptions.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[
            {"role": "system", "content": "You help users analyze CSV data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=400
    )
    return response.choices[0].message["content"]
