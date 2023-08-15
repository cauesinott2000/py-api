from typing import Union, Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


items: dict[int, dict[str, int | str] | dict[str, int | str]] = {
    1: {"item": "refrigerante", "preço": 6, "quantidade": 50},
    2: {"item": "ketchup", "preço": 4, "quantidade": 30}
}


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get("/items")
def read_all():
    return len(items)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
