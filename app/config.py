from pydantic import BaseSettings


# set environment variables. Must be set default settings
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # import environment variables from .env file
    class Config:
        env_file = '.env'


settings = Settings()
