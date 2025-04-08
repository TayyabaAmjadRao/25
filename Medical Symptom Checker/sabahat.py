import streamlit as st
import google.generativeai as genai
from langdetect import detect, DetectorFactory

# Configure Gemini AI
API_KEY = "AIzaSyBBTNFznyQOKaD56pYb-dXxwbp8bGYOXAI"  # Replace with your Gemini API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Supported Languages
languages = {
    "English": "English",
    "Urdu": "Urdu",
    "Sindhi": "Sindhi",
    "Punjabi (Shahmukhi)": "Punjabi",
    "Pashto": "Pashto",
    "Balochi": "Balochi",
    "Siraiki": "Siraiki",
    "Kashmiri": "Kashmiri",
    "Brahui": "Brahui",
    "Gujarati": "Gujarati",
    "Gilgiti": "Gilgiti",
    "Balti (Skardu)": "Balti",
    "Khowar (Chitrali)": "Khowar",
    "Shina": "Shina",
    "Hindko": "Hindko",
    "Potohari": "Potohari",
    "Wakhi": "Wakhi",
    "Torwali": "Torwali",
    "Burushaski": "Burushaski",
    "Rangri": "Rangri",
}

DetectorFactory.seed = 0  # Ensure consistent language detection

# Function to detect language
def detect_language(text):
    try:
        lang_code = detect(text)
        for key, value in languages.items():
            if value.lower().startswith(lang_code):
                return key
        return "Unknown"
    except:
        return "Unknown"

# Medical Symptom Checker Function
def check_medical_symptoms(symptoms, language):
    try:
        if not symptoms.strip():
            return "⚠ Please enter your symptoms."

        prompt = f"Analyze the following symptoms and provide medical advice in {language}. Your response should be entirely in {language}:\n\n{symptoms}"
        response = model.generate_content(prompt)

        if response and hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "⚠ Unable to analyze symptoms. Please try again."
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="🏥 AI Medical Symptom Checker", page_icon="⚕")
st.title("🏥 AI-Based Medical Symptom Checker")

# Text input
input_symptoms = st.text_area("📝 Describe your symptoms:")

# Detect language automatically
if input_symptoms.strip():
    detected_language = detect_language(input_symptoms)
    st.write(f"🌍 Detected Language: {detected_language}")
else:
    detected_language = "Unknown"

# Allow user to confirm or change detected language
language = st.selectbox("🌍 Select language:", options=languages.keys(), index=list(languages.keys()).index(detected_language) if detected_language in languages else 0)

# Analyze button
if st.button("🔍 Analyze Symptoms"):
    if input_symptoms.strip():
        result = check_medical_symptoms(input_symptoms, language)
        st.success(f"💊 *Medical Advice:*\n\n{result}")
    else:
        st.warning("⚠ Please enter your symptoms.")

# Footer
st.markdown("---")
st.markdown("🇵🇰 *Developed by SABAHAT* 🚀 | *Made with ❤ in Pakistan*")
