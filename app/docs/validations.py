from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(prefix="/val", tags=["val"])

#### Query Parameters and String Validations

@router.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=10)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#### Add Query to Annotated in the q parameter

@router.get("/items/two")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#### Add more validations

@router.get("/items/three")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=10)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#### Add regular expressions

@router.get("/items/four")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=10, pattern="^fixedquery$") #espera la palabra literal
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items/five")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results