from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://telemetry:telemetry_secret@localhost:5432/agentic_telemetry"
    app_title: str = "Agentic CI Observability"
    app_version: str = "1.0.0"

    # HTTP Basic Auth for dashboard (F7 — ADR-0007)
    # Set to empty string to disable auth (not recommended outside local dev)
    dashboard_username: str = ""
    dashboard_password: str = ""

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
