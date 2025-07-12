from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 80

    model_config = {
        "env_prefix": "NTFY_",
        "env_file": ".env",
        "extra": "allow"
    }

class NtfyConfig:
    port = Settings().port
    host = Settings().host