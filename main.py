from fastapi import FastAPI
from app.middleware.setup import setup_middlewares
from app.routers.router_conf import router
from app.app import fastapi_app


def setup_app() -> FastAPI:
    fastapi_app.include_router(router)
    setup_middlewares(fastapi_app)
    return fastapi_app


app: FastAPI = setup_app()
