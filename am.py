import streamlit as st
import google.generativeai as genai
from langdetect import detect

# Set up Gemini API Key
genai.configure(api_key="AIzaSyBBTNFznyQOKaD56pYb-dXxwbp8bGYOXAI")

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# Streamlit UI
st.set_page_config(page_title="AI Symptom Checker", page_icon="🩺")
st.title("🔥 AI-Powered Universal Language Symptom Checker 🔥")
st.write("Enter your symptoms in any language, and AI will analyze them!")

# User input
user_input = st.text_area("Describe your symptoms:")

if user_input:
    try:
        language = detect_language(user_input)
        st.write(f"Detected Language: {language}")
        
        # Generate response
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Analyze the following symptoms and provide possible diseases: {user_input}")
        
        # Display response
        st.subheader("Possible Conditions:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
