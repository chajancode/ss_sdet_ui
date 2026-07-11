from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    grid_url: str = 'http://localhost:4444/wd/hub'

    login: Optional[SecretStr] = None
    password: Optional[SecretStr] = None


settings = Settings()
