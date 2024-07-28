from fastapi import FastAPI
from app.lifespan import lifespan

fastapi_app = FastAPI(
    title="Check403Unlocker",
    lifespan=lifespan,
)
