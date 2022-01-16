import item as item
from fastapi import FastAPI

app = FastAPI() # FastAPI instance


@app.get("/") # path operation decorator
async def root(): # path operation function
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}