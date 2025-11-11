from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="Proyecto con FastAPI")

app.include_router(api_router, prefix="/api/docs")

@app.get("/")
async def root():
    return {"message": "Hello World"}


