from pydantic_settings import BaseSettings, ConfigDict

class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 80
    model_config = ConfigDict(extra='ignore')

    class Config:
        env_prefix = "NTFY_"
        env_file = ".env"

class NtfyConfig:
    port = Settings().port
    host = Settings().host