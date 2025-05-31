# openai_chat.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(prompt, context):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data expert who answers questions about CSV data."},
            {"role": "user", "content": f"Here is the CSV content:\n{context}\n\nQuestion: {prompt}"}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
