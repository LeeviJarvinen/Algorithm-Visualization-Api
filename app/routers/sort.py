from fastapi import APIRouter
from ..models.search import Request
from ..services import sort_service

router = APIRouter()

@router.post("/sort/bubble/", tags=['sort'])
async def bubble_sort_router(data: Request):
    return sort_service.bubble_sort(data)

@router.post("/sort/quick/", tags=['sort'])
async def bubble_sort_router(data: Request):
    return sort_service.quick_sort(data)
