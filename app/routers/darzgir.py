from fastapi import APIRouter , Depends
from app.services.handler import Handler
from app.routers.dependencies.get_httpx_client import get_httpx_client


from httpx import AsyncClient

router = APIRouter()


@router.get("/darzgir")
async def get_darzgir(url:str,client:AsyncClient = Depends(get_httpx_client)):
    obj_handler = Handler(client)

    result = await obj_handler.get_darzgir(url)

    return {"successful":result}


