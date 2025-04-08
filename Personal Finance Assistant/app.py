import streamlit as st
import google.generativeai as genai
import pandas as pd
import plotly.express as px

# Configure Gemini AI
GENAI_API_KEY = "AIzaSyBBTNFznyQOKaD56pYb-dXxwbp8bGYOXAI"
genai.configure(api_key=GENAI_API_KEY)

# Streamlit Page Config
st.set_page_config(page_title="VIP Personal Finance Assistant", page_icon="💰", layout="wide")

# Custom CSS for VIP Look
st.markdown(
    """
    <style>
        body {background-color: #f4f4f4;}
        .stApp {background-color: #ffffff; border-radius: 15px; padding: 20px;}
        .big-font {font-size:20px !important; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("💰 VIP Personal Finance Assistant")
st.write("Manage your finances smartly with AI-powered insights.")

# Expense Input
st.header("📊 Track Your Expenses")
category = st.selectbox("Select Category", ["Food", "Transport", "Entertainment", "Rent", "Others"])
amount = st.number_input("Enter Amount (in USD)", min_value=0.0, format="%.2f")
date = st.date_input("Select Date")

# Save Expenses
if st.button("Add Expense"):
    st.session_state.expenses.append({"Date": date, "Category": category, "Amount": amount})
    st.success("Expense Added Successfully!")

# Display Expenses
st.header("📈 Expense Overview")
if "expenses" not in st.session_state:
    st.session_state.expenses = []

df = pd.DataFrame(st.session_state.expenses)
if not df.empty:
    st.dataframe(df)
    fig = px.pie(df, names='Category', values='Amount', title='Expense Distribution')
    st.plotly_chart(fig)

# AI Financial Advice
st.header("🤖 AI Financial Advisor")
user_query = st.text_area("Ask AI about your finances:")
if st.button("Get Advice"):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_query)
        st.subheader("AI Response:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
