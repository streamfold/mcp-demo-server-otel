# MCP OpenTelemetry Server Demo

![Datadog Trace Waterfall](/contrib/trace.png)

Demonstration of a Remote MCP server instrumented with OpenTelemetry tracing and sending
traces to Datadog. This provides a single connected trace from MCP server through to
any backend APIs or databases giving you a complete understanding of your MCP server availability.

Features:

* Bundles a lightweight OpenTelemetry collector using [rotel](https://github.com/streamfold/pyrotel)
* Scripts that deploy to [Render](https://render.com/)
* Pushes trace spans to Datadog (using early experimental rotel trace support)
* Pulls the latest weather forecast from a configurable backend API

## Deploying to Render

1. Clone repo
2. Setup a new webservice in Render using the repo fork
3. Set the following Render properties:
   - Build script: `./scripts/render-build.sh`
   - Run script: `./scripts/render-start.sh`
4. Set the following environment variables:
   - `DATADOG_API_KEY`: Your Datadog API key
   - `DATADOG_REGION`: defaults to us1, options: us3, us5, eu, ap1
   - `WEATHER_API`: API endpoint of an API returning weather forecast given a zipcode
5. Deploy!

You can use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) to connect to your new MCP Server's
endpoint for testing. 

## TODO

This application **does not** include authentication/authorization support, so make sure to 
adjust to your particular needs. Cloudflare has [discussed](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/)
their recent approach for how to use an OAuth flow for MCP. 

## Developing

This project uses [uv](https://github.com/astral-sh/uv), to get started use `uv sync` to install dependencies.

