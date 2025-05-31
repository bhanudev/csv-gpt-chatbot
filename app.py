# app.py

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from openai_chat import ask_gpt

# Load .env for local dev (ignored in Streamlit Cloud)
load_dotenv()

# Get API key from Streamlit secrets (fallback to .env for local use)
openai_api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

# Set the API key as an env var (used in openai_chat.py)
os.environ["OPENAI_API_KEY"] = openai_api_key

st.set_page_config(page_title="CSV GPT Chatbot", layout="wide")
st.title("🤖 Chat with Your CSV (GPT-powered)")

st.markdown("Upload a CSV and ask GPT natural questions about your data.")

uploaded_file = st.file_uploader("📁 Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ CSV loaded successfully!")
    st.dataframe(df.head())

    user_question = st.text_input("💬 Ask something about the data:")
    if user_question:
        with st.spinner("🤖 GPT is thinking..."):
            answer = ask_gpt(user_question, df.head(10).to_string(index=False))
            st.markdown("### 🧠 GPT's Answer")
            st.write(answer)
else:
    st.info("👆 Please upload a CSV file to get started.")
