from fastapi import APIRouter
from .endpoints import article_router


api_v1_router = APIRouter(prefix="/api/1")
api_v1_router.include_router(article_router)
