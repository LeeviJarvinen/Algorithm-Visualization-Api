from fastapi import APIRouter
from ..models.search import SearchRequest
from ..services import sort

router = APIRouter()

@router.post("/sort/bubble/", tags=['sort'])
async def bubble_sort_router(data: SearchRequest):
    return sort.bubble_sort(data)

@router.post("/sort/quick/", tags=['sort'])
async def bubble_sort_router(data: SearchRequest):
    return sort.quick_sort(data)
