from contextlib import asynccontextmanager
from httpx import AsyncClient
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    app.state.httpx_client = AsyncClient()
    
    yield
    
    await app.state.httpx_client.aclose()
    
