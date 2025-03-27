import requests

from config import Settings


def get_forecast(settings: Settings, zipcode: str) -> dict:
    """Fetch the weather forecast for a given zipcode."""
    url = f"{settings.weather_api}/forecast/{zipcode}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()
