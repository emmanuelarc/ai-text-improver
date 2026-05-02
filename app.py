import streamlit as st
from openai import OpenAI
import os

# API KEY (local + cloud compatible)
api_key = None
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# UI
st.title("🔥 AI Hook Generator for Reels & TikTok")
st.write("Describe your content idea and get viral hooks to grab attention.")

idea = st.text_area("What is your video about?")

tone = st.selectbox(
    "Choose style:",
    ["Viral", "Controversial", "Motivational", "Funny"]
)

if st.button("Generate Hooks"):
    if idea.strip() == "":
        st.warning("Please describe your idea first.")
    else:
        prompt = f"""
        Generate 5 short, high-converting hooks for a TikTok/Reel.

        Topic: {idea}
        Style: {tone}

        Hooks should:
        - Be attention-grabbing
        - Be short (1–2 sentences max)
        - Make people want to keep watching
        """

        with st.spinner("Generating viral hooks..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        st.success(response.choices[0].message.content)