from fastapi import APIRouter

from src.api.v1.endpoints.server_endpoints import router as server_router
from src.api.v1.endpoints.user_endpoints import router as user_router

# -----------------------ROUTER--------------------
api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(server_router)
