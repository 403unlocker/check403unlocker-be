from fastapi import APIRouter

from app.routers.services import router as get_services
from app.routers.shecan import router as shecan_route
from app.routers.anti403 import router as anti403_route
from app.routers.vanilla import router as vanilla_route
from app.routers.begazar import router as begzar_route
from app.routers.begazar import router as begzar_route

router = APIRouter()


router.include_router(shecan_route)
router.include_router(anti403_route)
router.include_router(vanilla_route)
router.include_router(begzar_route)
router.include_router(get_services)
