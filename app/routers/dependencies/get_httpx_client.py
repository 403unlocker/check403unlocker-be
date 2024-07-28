from app.app import fastapi_app
from httpx import AsyncClient

def get_httpx_client() -> AsyncClient:
    return fastapi_app.state.httpx_client