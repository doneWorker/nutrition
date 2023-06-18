import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str
    host: str
    port: int
    db_url: str
    algorithm: str
    secret_key: str
    access_token_expire_minutes: int


@lru_cache()
def get_settings() -> Settings:
    """

    :rtype: object
    """
    # Load environment variables from {env_name}.env file
    env_path = f"{os.getenv('ENV_NAME', 'development')}.env"

    config_directory = os.path.abspath(env_path)
    print(f"Searching for config file in: {config_directory}")

    load_dotenv(dotenv_path=env_path)
    # Initialize Settings instance with environment variables or default values
    return Settings(
        env_name=os.getenv('ENV_NAME', 'development'),
        host=os.getenv('HOST', 'localhost'),
        port=os.getenv('PORT', 3000),
        algorithm=os.getenv('ALGORITHM', 'HS256'),
        secret_key=os.getenv('SECRET_KET', '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'),
        access_token_expire_minutes=os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 60 * 60 * 24 * 30),
        db_url=os.getenv('DB_URL', 'postgresql://user:password@localhost/dbname')
    )
