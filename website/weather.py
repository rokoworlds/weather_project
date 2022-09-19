import requests
from . import config

OWM_Endpoint = config.owm_endpoint
api_key = config.api_key


def weather_request(city_name):
  
    weather_params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    weather_info = f"Current temperature in {city_name} is: " + str(weather_data['main']["temp"]) + " °C " + "feels like: " + str(weather_data['main']['feels_like']) + " °C"
    return weather_info

