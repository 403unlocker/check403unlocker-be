from fastapi import APIRouter

from app.routers.schecan import router as schecan_route
from app.routers.anti403 import router as anti403_route
from app.routers.vanilla import router as vanilla_route
from app.routers.bagazar import router as bagzar_route


router = APIRouter()


router.include_router(schecan_route)
router.include_router(anti403_route)
router.include_router(vanilla_route)
router.include_router(bagzar_route)
