import streamlit as st
import google.generativeai as genai

# Set up Gemini API Key
GENAI_API_KEY = "AIzaSyBBTNFznyQOKaD56pYb-dXxwbp8bGYOXAI"  # Apna API key yahan replace karein
genai.configure(api_key=GENAI_API_KEY)

# Streamlit UI
st.set_page_config(page_title="Travel Guide Chatbot")
st.title("🌍 Travel Guide Chatbot")
st.write("Ask me anything about travel destinations, tips, and itineraries!")

# User input
user_input = st.text_input("Enter your travel query:")

if user_input:
    try:
        # Generate response using Gemini 1.5 Flash
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        
        # Display response
        st.subheader("Chatbot Response:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
