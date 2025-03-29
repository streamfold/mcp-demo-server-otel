import re

from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount, Host, Route
from src.client import get_forecast

from opentelemetry import trace

from config import Settings
from src.tracing import enable_tracing

settings = Settings()

if settings.enable_tracing:
    enable_tracing(settings)

tracer = trace.get_tracer("mcp.tracer")

mcp = FastMCP("MCP Demo Weather")

@mcp.resource("resource://{zipcode}/weather")
@tracer.start_as_current_span("weather_resource")
def weather_resource(zipcode: str) -> str:
    if not re.fullmatch(r'[0-9]{5}', zipcode):
        return f"{zipcode} is not a valid zipcode"
    current_span = trace.get_current_span()
    current_span.set_attribute("operation.zipcode", zipcode)
    try:
        forecast = get_forecast(settings, zipcode)
        detailed_forecast = forecast["properties"]["periods"][0]["detailedForecast"]
        return f"The forecast for zipcode {zipcode} is: {detailed_forecast}"
    except Exception as e:
        return str(e)

# Mount the SSE server to the existing ASGI server
app = Starlette(debug=True,
                routes=[
                    Mount('/', app=mcp.sse_app()),
                ])

if __name__ == "__main__":
    mcp.run()
