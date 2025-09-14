from fastapi import APIRouter
from ..models.search import Request
from ..services import search_service

router = APIRouter()

@router.post("/search/linear", tags=['search'])
async def linear_search_router(data: Request):
    return search_service.linear_search(data)

@router.post("/search/binary", tags=['search'])
async def binary_search_router(data: Request):
    return search_service.binary_search(data)
