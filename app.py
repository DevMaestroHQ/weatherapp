import streamlit as st
from datetime import datetime
from weather_api import get_weather_forecast, get_air_quality, get_astronomy_data
from utils import load_preferences, save_preferences
import pandas as pd
import plotly.express as px
import json

# Load labels
with open("labels.json", "r", encoding="utf-8") as f:
    labels = json.load(f)

# Set page config
st.set_page_config(page_title="WeatherStrike", layout="wide")

# Load user preferences
prefs = load_preferences()
def_city = prefs.get("city", "Kathmandu")
unit = st.sidebar.selectbox("Unit", ["C", "F"], index=0 if prefs.get("unit") == "C" else 1)
lang = st.sidebar.selectbox("Language", ["English", "Nepali"], index=0 if prefs.get("lang") == "English" else 1)
L = labels[lang]

# City input form for real-time update
with st.form("city_form"):
    city_input = st.text_input(f"{L['current_weather']}", def_city)
    submitted = st.form_submit_button("Get Weather")
    if submitted:
        save_preferences(city_input, unit, lang)
        city = city_input
    else:
        city = def_city

# Fetch real-time data
current, forecast_days = get_weather_forecast(city, days=7)
air_quality = get_air_quality(city)
astro = get_astronomy_data(city)

# --- Custom CSS for modern design ---
st.markdown("""
<style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .forecast-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: stretch;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 16px;
        padding-bottom: 20px;
        margin-top: 20px;
    }
    .forecast-card {
        background-color: rgba(255, 255, 255, 0.15);
        padding: 18px;
        width: 180px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        backdrop-filter: blur(8px);
        transition: all 0.3s ease;
        flex-shrink: 0;
    }
    .forecast-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .extras-container {
        display: flex;
        justify-content: space-around;
        margin-top: 40px;
        flex-wrap: wrap;
    }
    .extras-card {
        background-color: rgba(255,255,255,0.1);
        padding: 25px;
        border-radius: 18px;
        min-width: 260px;
        text-align: left;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        backdrop-filter: blur(10px);
        margin: 10px;
    }
    .extras-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .metric-box {
        display: flex;
        gap: 30px;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- Display Current Weather ---
st.markdown(f"### {L['current_weather']} {city}")
st.markdown('<div class="metric-box">', unsafe_allow_html=True)
st.metric(label=L['temperature'], value=f"{current['temp_c'] if unit == 'C' else current['temp_f']}°{unit}")
st.metric(label=L['humidity'], value=f"{current['humidity']}%")
st.metric(label=L['wind'], value=f"{current['wind_kph']} km/h")
st.markdown('</div>', unsafe_allow_html=True)

# --- 7-Day Forecast ---
st.markdown(f"### {L['forecast']}")
st.markdown('<div class="forecast-container">', unsafe_allow_html=True)
for day in forecast_days:
    date = day['date']
    icon = day['day']['condition']['icon']
    text = day['day']['condition']['text']
    max_temp = day['day']['maxtemp_f'] if unit == "F" else day['day']['maxtemp_c']
    min_temp = day['day']['mintemp_f'] if unit == "F" else day['day']['mintemp_c']
    st.markdown(f"""
    <div class="forecast-card">
        <img src="{icon}" alt="icon">
        <p><strong>{date}</strong></p>
        <p>{text}</p>
        <p><strong>Max:</strong> {max_temp}°{unit}</p>
        <p><strong>Min:</strong> {min_temp}°{unit}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Historical Line Chart ---
st.markdown(f"### {L['hourly_chart']}")
history_df = pd.DataFrame([{
    "Date": d["date"],
    "Max": d["day"]["maxtemp_f"] if unit == "F" else d["day"]["maxtemp_c"],
    "Min": d["day"]["mintemp_f"] if unit == "F" else d["day"]["mintemp_c"]
} for d in forecast_days])
fig = px.line(history_df, x="Date", y=["Max", "Min"], markers=True,
              labels={"value": f"Temperature (°{unit})", "Date": "Date", "variable": "Type"})
st.plotly_chart(fig, use_container_width=True)

# --- Extras: Air Quality and Astronomy ---
st.markdown(f"### {L['air_quality']} & {L['astronomy']}")
st.markdown(f"""
<div class="extras-container">
    <div class="extras-card">
        <h4>{L['air_quality']}</h4>
        <p>PM2.5: <strong>{air_quality['pm2_5']}</strong></p>
        <p>PM10: <strong>{air_quality['pm10']}</strong></p>
        <p>CO: <strong>{air_quality['co']}</strong></p>
    </div>
    <div class="extras-card">
        <h4>{L['astronomy']}</h4>
        <p>🌅 {L['sunrise']}: <strong>{astro['sunrise']}</strong></p>
        <p>🌇 {L['sunset']}: <strong>{astro['sunset']}</strong></p>
        <p>🌘 {L['moon_phase']}: <strong>{astro['moon_phase']}</strong></p>
    </div>
</div>
""", unsafe_allow_html=True)