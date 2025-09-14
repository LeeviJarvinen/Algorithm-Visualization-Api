from fastapi import FastAPI
from .routers import sort, search

app = FastAPI()

API_PREFIX = "/api/v1"

app.include_router(sort.router, prefix=API_PREFIX)
app.include_router(search.router, prefix=API_PREFIX)
