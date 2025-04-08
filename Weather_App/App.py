import streamlit as st
import requests

# OpenWeatherMap API Key (Replace with your actual API key)
API_KEY = "cb771e45ac79a4e8e2205c0ce66ff633"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch city names dynamically
@st.cache_data
def get_cities():
    url = "https://countriesnow.space/api/v0.1/countries/population/cities"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cities = sorted([city["city"] for city in data["data"]])
        return cities
    else:
        return ["Karachi", "Lahore", "New York", "London", "Tokyo"]  # Fallback cities

# Fetch all cities
cities = get_cities()

# Streamlit UI with styled header
st.markdown(
    "<h1 style='text-align: center; color: #FF9800;'>🌤️ Live Weather App</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p style='text-align: center; color: #757575;'>Get real-time weather updates for any city worldwide 🌍</p>",
    unsafe_allow_html=True,
)

# City selection dropdown (Dynamically fetched)
city = st.selectbox("🏙️ Select a City", cities)

if st.button("🔍 Get Weather"):
    if city:
        try:
            # API request
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if response.status_code == 200:
                # Extract weather details
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                pressure = data["main"]["pressure"]
                weather_desc = data["weather"][0]["description"].title()

                # Weather Icon
                icon_code = data["weather"][0]["icon"]
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

                # Display results with styling
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <h2 style="color: #4CAF50;">🌍 {city}</h2>
                        <img src="{icon_url}" width="100">
                        <h3 style="color: #2196F3;">{weather_desc}</h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f"""
                    <div style="background-color: #f1f1f1; padding: 15px; border-radius: 10px;">
                        <h4>🌡 Temperature: <b>{temp}°C</b></h4>
                        <h4>💧 Humidity: <b>{humidity}%</b></h4>
                        <h4>💨 Wind Speed: <b>{wind_speed} m/s</b></h4>
                        <h4>🌬 Air Pressure: <b>{pressure} hPa</b></h4>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:
                st.error("❌ City not found. Please try again.")

        except Exception as e:
            st.error(f"⚠ Error fetching weather data: {e}")

# Footer with styling
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>Developed by <b>Muhammad Mudasir</b> | Powered by OpenWeatherMap</p>",
    unsafe_allow_html=True,
)
