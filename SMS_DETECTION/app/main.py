from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="SMS Spam Classifier API")

app.include_router(router)
