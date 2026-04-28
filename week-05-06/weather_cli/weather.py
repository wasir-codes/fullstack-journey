from decouple import config
import requests
from requests.exceptions import ConnectionError, Timeout

API_KEY = config("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        return response
    except ConnectionError:
        print("\n❌ No internet connection. Please check your network.\n")
        return None
    except Timeout:
        print("\n❌ Request timed out. The server took too long to respond.\n")
        return None

def display_weather(data):
    city = data['name']
    country = data['sys']['country']
    description = data['weather'][0]['description'].capitalize()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    visibility_km = data['visibility'] / 1000

    print(f"\n📍 {city}, {country}")
    print(f"⛅ {description}")
    print(f"🌡 Temperature : {temp}°C (feels like {feels_like}°C)")
    print(f"💧 Humidity    : {humidity}%")
    print(f"💨 Wind speed  : {wind_speed} m/s")
    print(f"👁 Visibility  : {visibility_km} km\n")

city = input("Enter city name: ")
response = get_weather(city)

if response is None:
    pass
elif response.status_code == 404:
    print(f"\n❌ City '{city}' not found. Check the spelling and try again.\n")
elif response.status_code != 200:
    print(f"\n❌ Unexpected error. Status code: {response.status_code}\n")     
else:
    data = response.json()
    display_weather(data)