from fastapi import APIRouter
from ..models.sort import NumRequest
from ..services import sort

router = APIRouter()

@router.post("/bubble/", tags=['sort'])
async def bubble_sort_router(data: NumRequest):
    return sort.bubble_sort(data)

@router.post("/quick/", tags=['sort'])
async def bubble_sort_router(data: NumRequest):
    return sort.quick_sort(data)
