from config import Settings

from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource, DEPLOYMENT_ENVIRONMENT
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

def enable_tracing(settings: Settings):
    from rotel import Config, Rotel

    # Send traces to Axiom
    rotel = Rotel(
        enabled=True,
        debug_log=["traces"],
        exporter=Config.datadog_exporter(
            region=settings.datadog_region,
            api_key=settings.datadog_api_key,
        )
    )
    rotel.start()

    # Set up the OpenTelemetry tracer provider with a resource name.
    resource = Resource(attributes={
        SERVICE_NAME: "mcp-demo-server-otel",
        DEPLOYMENT_ENVIRONMENT: "dev",
    })
    provider = TracerProvider(resource=resource)

    span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces"))
    provider.add_span_processor(span_processor)

    trace.set_tracer_provider(provider)

    RequestsInstrumentor().instrument()

