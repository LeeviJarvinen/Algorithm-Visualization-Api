from fastapi import APIRouter
from ..models.search import SearchRequest
from ..services import search

router = APIRouter()

@router.post("/search/linear", tags=['search'])
async def linear_search_router(data: SearchRequest):
    return search.linear_search(data)

@router.post("/search/binary", tags=['search'])
async def binary_search_router(data: SearchRequest):
    return search.binary_search(data)
