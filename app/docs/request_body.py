from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/body", tags=["body"])

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@router.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

##### request body + path parameters

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

##### request body + path + query parameters

@router.put("/item/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
