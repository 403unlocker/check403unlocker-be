import asyncio
from fastapi import APIRouter , Depends
from app.services.handler import Handler
from app.routers.dependencies.get_httpx_client import get_httpx_client


from httpx import AsyncClient

router = APIRouter()



@router.get("/services")
async def get_services(url:str,client:AsyncClient = Depends(get_httpx_client)):
    obj_handler = Handler(client)

    shecan_task = obj_handler.get_shecan(url)
    begzar_task = obj_handler.get_begzar(url)
    anti403_task = obj_handler.get_anti403(url)
    darzgir_task = obj_handler.get_darzgir(url)
    # vanillapp_task = obj_handler.get_vanilla(url)



    begzarResponse, anti403Response, shecanResponse, darzgirResponse = await asyncio.gather(
        begzar_task, 
        anti403_task, 
        shecan_task,
        darzgir_task
        # vanillapp_task
    )

    return {"services": {
        "begzar": begzarResponse,
        "anti403": anti403Response,
        "shecan": shecanResponse,
        "darzgir": darzgirResponse,
        # "vanillapp": vanillappResponse,
    }}
