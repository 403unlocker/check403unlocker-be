from fastapi import APIRouter , Depends
from app.services.handler import Handler
from app.routers.dependencies.get_httpx_client import get_httpx_client


from httpx import AsyncClient

router = APIRouter()


@router.get("/begzar")
async def get_begzar(url:str,client:AsyncClient = Depends(get_httpx_client)):
    obj_handler = Handler(client)

    result = await obj_handler.get_begzar(url)

    return {"IsSuccess":result}


