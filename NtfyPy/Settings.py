from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 80

    class Config:
        env_prefix = "NTFY_"
        env_file = ".env"

class NtfyConfig:
    port = Settings().port
    host = Settings().host