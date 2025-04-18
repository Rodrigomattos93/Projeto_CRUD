from fastapi import FastAPI
from db import engine
import models
from routers import router

models.Base.metadase.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
