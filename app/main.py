from fastapi import FastAPI
from app.db import engine
import app.models
from app.routers import router

app.models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
