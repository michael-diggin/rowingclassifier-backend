from fastapi import Security, HTTPException
import os
from fastapi.security.api_key import APIKey, APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseSettings
from functools import lru_cache


class APISettings(BaseSettings):
    API_KEY: str = os.getenv('API_KEY')
    API_KEY_NAME: str = "X-API-KEY"

settings = APISettings()

api_key_header = APIKeyHeader(name=settings.API_KEY_NAME)


async def check_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != settings.API_KEY:
        raise HTTPException(HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    return api_key_header