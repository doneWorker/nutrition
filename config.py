import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str
    host: str
    port: int
    db_url: str


@lru_cache
def get_settings() -> Settings:
    """

    :rtype: object
    """
    # Load environment variables from {env_name}.env file
    env_path = f"{os.getenv('ENV_NAME', 'development')}.env"
    load_dotenv(dotenv_path=env_path)

    # Initialize Settings instance with environment variables or default values
    return Settings(
        env_name=os.getenv('ENV_NAME', 'development'),
        host=os.getenv('HOST', 'localhost'),
        port=os.getenv('PORT', 3000),
        db_url=os.getenv('DB_URL', 'postgresql://user:password@localhost/dbname')
    )
