from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKey, APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseSettings
from functools import lru_cache


class APISettings(BaseSettings):
    API_KEY: str = None
    API_KEY_NAME: str = None

    class Config:
        env_file = ".env"

@lru_cache()
def set_settings():
    return APISettings()



api_key_header = APIKeyHeader(name=set_settings().API_KEY_NAME)


async def check_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != set_settings().API_KEY:
        raise HTTPException(HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    return api_key_header