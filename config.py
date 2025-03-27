from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    weather_api: str = ""

    enable_tracing: bool = False

    datadog_region: str = "us1"
    datadog_api_key: str = ""
