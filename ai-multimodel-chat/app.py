

import streamlit as st
import requests

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

MODELS = [
    "gpt-4o-mini",
    "gpt-4o",
    "gpt-3o-mini",
    "gpt-3o",
    "gpt-3o-large"
]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_response(prompt, model):
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f8ff;
            color: #333333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.title("🤖 Multi-Model Chat with OpenRouter")

    prompt = st.text_area("Enter your prompt here:", height=120)

    if st.button("Get Responses"):
        if not prompt.strip():
            st.warning("Please enter a prompt!")
            return
        
        for model in MODELS:
            st.markdown(f"<h3 style='color: #2F4F4F;'>Model: <code>{model}</code></h3>", unsafe_allow_html=True)
            result = get_response(prompt, model)
            st.markdown(f"<p style='background-color:#e0f7fa; padding:10px; border-radius:8px;'>{result}</p>", unsafe_allow_html=True)
            st.markdown("---")

if __name__ == "__main__":
    main()
