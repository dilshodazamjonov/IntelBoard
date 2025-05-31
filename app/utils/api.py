from fastapi import FastAPI
from app.routes.location import router

def register_router(app: FastAPI):
    app.include_router(router)
    app.include_router(router)


