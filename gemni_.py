import google.generativeai as genai
import streamlit as st

# Function to generate AI response
def apiai(prompt):
    api_key = "AIzaSyBUOfYKrZWcjme8mDlcFU3GTgJt97Bl2os"  # Ideally move to st.secrets or .env

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.title("Gemini API AI")
st.write("This is a simple Streamlit app to interact with the Gemini API. MADE BY PRATHAM GOYAL...")
prompt = st.text_area("Enter your prompt", height=100, placeholder="Type your prompt here...")

if st.button("Submit"):
    if prompt:
        with st.spinner("Generating response..."):
            response = apiai(prompt)

        if response:
            st.success("Response generated successfully.")
            st.write("Response:")
            st.chat_message("user").markdown(prompt)
            st.chat_message("assistant").markdown(response)
        else:
            st.error("No response received.")
    else:
        st.error("Please enter a prompt before submitting.")
