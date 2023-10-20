from fastapi import APIRouter

from api.http.routers.v1 import book

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(book.router)
