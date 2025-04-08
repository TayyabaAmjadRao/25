import streamlit as st
import google.generativeai as genai
from langdetect import detect

# Set up Gemini AI API Key
GENAI_API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=GENAI_API_KEY)

# Streamlit UI Setup
st.set_page_config(page_title="AI-Powered Symptom Checker", page_icon="🩺")
st.title("🔥 AI-Powered Universal Language Symptom Checker 🔥")
st.write("Enter your symptoms in any language, and AI will analyze them.")

# Language Selection
languages = {
    "Auto-Detect": "auto",
    "English": "en",
    "Urdu": "ur",
    "Sindhi": "sd",
    "Punjabi": "pa",
    "Pashto": "ps",
    "Balochi": "bal",
    "Kashmiri": "ks",
    "Saraiki": "skr",
    "Brahui": "brh",
    "Gujarati": "gu",
    "Gilgiti": "glk",
    "Balti": "bft",
    "Khowar": "khw",
    "Shina": "scl",
    "Hindko": "hno",
    "Potohari": "phr",
    "Wakhi": "wbl",
    "Torwali": "trw",
    "Burushaski": "bsk"
}
selected_language = st.selectbox("Select Language (or Auto-Detect)", list(languages.keys()))

# User Input
user_input = st.text_area("Describe your symptoms:")

if user_input:
    try:
        # Detect Language if Auto-Detect is selected
        detected_language = detect(user_input) if selected_language == "Auto-Detect" else languages[selected_language]
        st.write(f"Detected/Selected Language: {detected_language}")
        
        # AI Symptom Analysis using Gemini-Pro
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Analyze the following symptoms and provide a possible diagnosis and risk level. Language: {detected_language}. Symptoms: {user_input}")
        
        # Display AI Response
        st.subheader("AI Analysis:")
        st.write(response.text if hasattr(response, 'text') else "No response from AI.")
    except Exception as e:
        st.error(f"Error: {e}")
