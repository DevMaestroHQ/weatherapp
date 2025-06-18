import requests

API_KEY = "075052bc3f3e479796210737251706"
BASE_URL = "http://api.weatherapi.com/v1"

def get_weather_forecast(city, days=7):
    url = f"{BASE_URL}/forecast.json?key={API_KEY}&q={city}&days={days}&aqi=yes&alerts=no"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["current"], data["forecast"]["forecastday"]

def get_air_quality(city):
    url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=yes"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["current"]["air_quality"]
    return {
        "co": round(data["co"], 2),
        "pm2_5": round(data["pm2_5"], 2),
        "pm10": round(data["pm10"], 2)
    }

def get_astronomy_data(city):
    url = f"{BASE_URL}/astronomy.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    response.raise_for_status()
    astro = response.json()["astronomy"]["astro"]
    return {
        "sunrise": astro["sunrise"],
        "sunset": astro["sunset"],
        "moon_phase": astro["moon_phase"]
    }
