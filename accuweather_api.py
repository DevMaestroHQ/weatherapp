import requests

API_KEY = "w659Ccwutl7tm4TEr3tq6rGLhzYiXX6R"
BASE_URL = "http://dataservice.accuweather.com"

def get_location_key(city):
    url = f"{BASE_URL}/locations/v1/cities/search"
    params = {"apikey": API_KEY, "q": city}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data[0]["Key"] if data else None

def get_current_weather(location_key):
    url = f"{BASE_URL}/currentconditions/v1/{location_key}"
    params = {"apikey": API_KEY, "details": True}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[0]

def get_daily_forecast(location_key, days=5):
    url = f"{BASE_URL}/forecasts/v1/daily/{days}day/{location_key}"
    params = {"apikey": API_KEY, "metric": True}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["DailyForecasts"]