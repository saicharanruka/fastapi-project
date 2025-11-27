from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # Use SettingsConfigDict for Pydantic v2
    # extra='ignore' is good practice to avoid errors if you have extra env vars
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_ignore_empty=True,
        extra="ignore"
    )

settings = Settings()