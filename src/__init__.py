from fastapi import FastAPI
from src.application import controller


app = FastAPI()
app.include_router(controller.router)
