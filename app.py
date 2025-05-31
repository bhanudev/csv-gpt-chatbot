import streamlit as st
import pandas as pd
from openai_chat import ask_gpt
import os

# Use Streamlit Secrets instead of dotenv
openai_api_key = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = openai_api_key

st.set_page_config(page_title="CSV GPT Chatbot", layout="wide")
st.title("🤖 Chat with Your CSV (GPT-powered)")

st.markdown("Upload a CSV and ask GPT natural questions about your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("CSV loaded successfully!")
    st.dataframe(df.head())

    user_question = st.text_input("Ask something about the data:")
    if user_question:
        with st.spinner("Thinking..."):
            answer = ask_gpt(user_question, df.head(10).to_string(index=False))
            st.markdown("### 🧠 GPT's Answer")
            st.write(answer)
else:
    st.info("Please upload a CSV file to get started.")
