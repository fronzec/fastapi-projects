from typing import Optional, List
from enum import Enum
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# FastAPI instance
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")  # path operation decorator
async def root():  # path operation function
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/list/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


@app.get("/itemsv3/")
async def read_items(
        q: Optional[str] = Query(
            None,
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            regex="^fixedquery$",
            deprecated=True,
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/v2/items/{item_id}")
async def read_user_item_v2(
        item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.get("/products/{item_id}")
async def read_product(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.put("/itemsoptional/{item_id}")
async def update_item(item_id: int, item: Optional[Item] = None):
    return {"item_id": item_id, **item.dict()}


@app.put("/items/multibody/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body(...),q: Optional[str] = None):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q":q})
    return results


@app.put("/items/embed/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results



@app.put("/items2/{item_id}")
async def create_item2(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items5/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000), q: str,
    size: float = Query(..., gt=0, le=10.5)
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results