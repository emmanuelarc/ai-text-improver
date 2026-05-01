import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("AI Text Improver")

user_input = st.text_area("Write something:")

tone = st.selectbox(
    "Choose style:",
    ["Professional", "Casual", "Charismatic"]
)

if st.button("Improve"):
    if user_input.strip() == "":
        st.warning("Please write something first.")
    else:
        prompt = f"Rewrite this text in a {tone.lower()} way: {user_input}"

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.write(response.choices[0].message.content)