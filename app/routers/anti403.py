from fastapi import APIRouter , Depends
from app.services.handler import Handler
from app.routers.dependencies.get_httpx_client import get_httpx_client


from httpx import AsyncClient

router = APIRouter()


@router.get("/anti403")
async def get_anti403(url:str,client:AsyncClient = Depends(get_httpx_client)):
    obj_handler = Handler(client)

    result = await obj_handler.get_anti403(url)

    return {"IsSuccess":result}


