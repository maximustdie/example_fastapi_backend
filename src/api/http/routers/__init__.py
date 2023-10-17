from fastapi import APIRouter
from api.http.routers import health


root_router = APIRouter(prefix="/api")

root_router.include_router(health.router)
