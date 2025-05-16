import google.generativeai as genai
import streamlit as st

# Function to generate AI response
def get_gemini_response(prompt):
    try:
        # Configure with API key from secrets
        genai.configure(api_key="AIzaSyBUOfYKrZWcjme8mDlcFU3GTgJt97Bl2os")
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI setup
st.title("Gemini API Chat")
st.write("A simple chat interface for Gemini AI. Made by Pratham Goyal.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_gemini_response(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
