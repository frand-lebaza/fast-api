from fastapi import APIRouter
from app.docs import path_parameters, query_parameters, request_body, validations

api_router = APIRouter()

api_router.include_router(path_parameters.router)
api_router.include_router(query_parameters.router)
api_router.include_router(request_body.router)
api_router.include_router(validations.router)