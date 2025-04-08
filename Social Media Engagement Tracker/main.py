import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="📊 Social Media Engagement Tracker", layout="wide")

# Custom CSS for VIP styling
st.markdown("""
    <style>
        body { background-color: #f8f9fa; }
        .stApp { background-color: white; border-radius: 15px; padding: 20px; }
        h1 { color: #FF5733; text-align: center; }
        .css-1d391kg { padding: 2rem; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("📊 Social Media Engagement Tracker")
st.write("Analyze your engagement data and gain insights into your social media performance.")

# File upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

def load_data(file):
    return pd.read_csv(file)

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("File uploaded successfully!")
    
    # Show Dataframe
    st.subheader("📌 Raw Data")
    st.dataframe(df)
    
    # Select engagement metric
    metric = st.selectbox("Select metric to analyze", df.columns[1:])
    
    # Generate Plot
    fig = px.line(df, x=df.columns[0], y=metric, title=f"Engagement Trend for {metric}", markers=True)
    st.plotly_chart(fig)
    
    # Display Summary Statistics
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())
