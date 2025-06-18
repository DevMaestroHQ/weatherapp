import json
import os

PREF_FILE = "preferences.json"

def save_preferences(city, unit, lang="English"):
    prefs = {"city": city, "unit": unit, "lang": lang}
    with open(PREF_FILE, "w") as f:
        json.dump(prefs, f)

def load_preferences():
    if os.path.exists(PREF_FILE):
        with open(PREF_FILE, "r") as f:
            return json.load(f)
    return {"city": "Kathmandu", "unit": "C", "lang": "English"}
