# Weather CLI App

A command-line weather app built with Python that fetches real-time 
weather data from the OpenWeatherMap API.

## Features
- Current temperature and feels-like temperature
- Humidity, wind speed, and visibility
- Handles invalid city names gracefully
- Handles no internet connection gracefully
- API key stored securely in .env file

## Tech Stack
- Python 3.14
- requests
- python-decouple

## Setup

1. Clone the repository
    
    git clone <your-repo-url>
    cd weather_cli

2. Create and activate virtual environment

    python -m venv venv
    venv\Scripts\activate

3. Install dependencies

    pip install -r requirements.txt

4. Get a free API key from https://openweathermap.org

5. Create a .env file in the project root
    
    Write this line with your api key in the .env file:

        API_KEY=your_api_key_here

6. Run the app

    python weather.py

## Example Output

📍 Dhaka, BD
🌤  Overcast clouds
🌡  Temperature : 24.98°C (feels like 25.73°C)
💧  Humidity    : 84%
💨  Wind speed  : 2.2 m/s
👁  Visibility  : 10.0 km

## What I learned
- Proper usage of REST API (requests library)
- Handling multiple error cases as required - in this app (invalid city, no internet, timeout)
- Storing secrets securely using .env and python decouple
- Setting up virtual environment(venv)
