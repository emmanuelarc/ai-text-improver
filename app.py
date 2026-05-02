import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Text Improver")
st.write("Paste your text below and choose a style. The AI will rewrite it for you.")

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

        with st.spinner("Improving your text..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        st.success(response.choices[0].message.content)