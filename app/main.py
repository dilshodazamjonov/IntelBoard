from fastapi import FastAPI
from app.utils.api import register_router
app = FastAPI()


register_router(app)