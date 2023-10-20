from fastapi import APIRouter

from api.http.routers import health
from api.http.routers.v1 import v1_router


root_router = APIRouter(prefix="/api")

root_router.include_router(health.router)
root_router.include_router(v1_router)
