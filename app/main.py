from fastapi import FastAPI
from .routers import sort, search

app = FastAPI()


app.include_router(sort.router, prefix='/api')
app.include_router(search.router, prefix='/api')
