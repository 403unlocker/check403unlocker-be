import asyncio
from fastapi import APIRouter , Depends
from app.services.handler import Handler
from app.routers.dependencies.get_httpx_client import get_httpx_client


from httpx import AsyncClient

router = APIRouter()



@router.get("/services")
async def get_services(url:str,client:AsyncClient = Depends(get_httpx_client)):
    obj_handler = Handler(client)

    begzar_task = obj_handler.get_begzar(url)
    anti403_task = obj_handler.get_anti403(url)
    shecan_task = obj_handler.get_shecan(url)
    # vanillapp_task = obj_handler.get_vanilla(url)

    begzarResponse, anti403Response, shecanResponse = await asyncio.gather(
        begzar_task, 
        anti403_task, 
        shecan_task
        # vanillapp_task
    )

    return {"services": {
        "begzar": begzarResponse,
        "anti403": anti403Response,
        "shecan": shecanResponse,
        # "vanillapp": vanillappResponse,
    }}
