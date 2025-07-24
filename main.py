from fastapi import FastAPI
from routers import sandwich
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(sandwich.router)
